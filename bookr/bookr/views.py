# from xlsxwriter import Workbook
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
import plotly.graph_objects as graphs
from io import BytesIO

from .utils import get_books_read_by_month, get_books_read


@login_required
def profile(request):
    user = request.user
    permissions = user.get_all_permissions()
    books_read_by_month = get_books_read_by_month(user.username)
    months = [i+1 for i in range(12)]
    books_read = [0 for _ in range(12)]

    for num_books_read in books_read_by_month:
        list_index = num_books_read['date_created__month'] - 1
        books_read[list_index] = num_books_read['book_count']

    figure = graphs.Figure()
    scatter = graphs.Scatter(x=months, y=books_read)
    figure.add_trace(scatter)
    figure.update_layout(xaxis_title="Month", yaxis_title="No. of books read")
    plot_html = plot(figure, output_type="div")

    context = {
        "user": user,
        "permissions": permissions,
        "books_read_plot": plot_html
    }
    return render(request, 'profile.html', context=context)

@login_required
def reading_history(request):
    user = request.user.username
    books_read = get_books_read(user)

    temp_file = BytesIO()

    workbook = Workbook(temp_file)
    worksheet = workbook.add_worksheet()

    data = []
    for book_read in books_read:
        data.append([book_read['title'],str(book_read['completed_on'])])

    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row, col, data[row][col])

    workbook.close()
    data_to_download = temp_file.getvalue()

    response = HttpResponse(content_type='aplication/vnd.ms-excel')
    response['Content-Disposition'] = 'atachement; filename=reading_history.xlsx'
    response.write(data_to_download)
    return response
