from django.contrib import admin
from .models import Author, Book, Review


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'birth_date', 'created_at']
    list_filter = ['created_at', 'birth_date']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'bio', 'birth_date')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'price', 'is_available', 'publication_date']
    list_filter = ['genre', 'is_available', 'publication_date', 'created_at']
    search_fields = ['title', 'author__name', 'isbn']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_available', 'price']
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'isbn', 'genre')
        }),
        ('Details', {
            'fields': ('description', 'publication_date', 'pages', 'price', 'is_available')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'book__genre']
    search_fields = ['book__title', 'user__username', 'comment']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('book', 'user', 'rating', 'comment')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
