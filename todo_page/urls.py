from django.urls import path

from todo_page.views import TagListView, TaskListView, TagCreateView, TagUpdateView, TagDeleteView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView, ChangeStatusView

urlpatterns = [
    path("tags/", TagListView.as_view(), name="tag_list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),

    path("", TaskListView.as_view(), name="task_list"),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "<int:pk>/change_status/",
        ChangeStatusView.as_view(),
        name="change_task_status"

    )
]

app_name = "todo_page"
