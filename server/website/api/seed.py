from .models import Category

def create_data():
    categories = [
        {'name': 'Technology', 'slug': 'technology'},
        {'name': 'Health', 'slug': 'health'},
        {'name': 'Education', 'slug': 'education'},
        {'name': 'Sports', 'slug': 'sports'},
        {'name': 'Entertainment', 'slug': 'entertainment'},
    ]

    for data in categories:
        category, created = Category.objects.get_or_create(
            name=data['name'],
            slug=data['slug'],
        )
        if created:
            print(f'"{category.name}" created.')
        else:
            print(f'"{category.name}" already exists.')
