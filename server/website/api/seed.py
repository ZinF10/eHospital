from .models import Category, Doctor, Nurse, Department, User


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

    users = [
        {'email': 'alice@gmail.com', 'username': 'alice',
            'first_name': 'Alice', 'last_name': 'Johnson'},
        {'email': 'bob@gmail.com', 'username': 'bob',
            'first_name': 'Bob', 'last_name': 'Williams'},
        {'email': 'john@gmail.com', 'username': 'john',
            'first_name': 'John', 'last_name': 'Doe'},
        {'email': 'smith@gmail.com', 'username': 'smith',
            'first_name': 'Jane', 'last_name': 'Smith'},
    ]

    for data in users:
        user, created = User.objects.get_or_create(
            email=data['email'],
            defaults={
                'username': data['username'],
                'first_name': data['first_name'],
                'last_name': data['last_name']
            }
        )
        if created:
            user.set_password('123')
            user.save()
            print(f'User {user.get_full_name()} created with password "123".')
        else:
            print(f'User {user.get_full_name()} already exists.')

    doctors = [
        {'user': 2, 'department_name': 'Cardiology'},
        {'user': 3, 'department_name': 'Neurology'},
    ]

    for data in doctors:
        department_name = data.pop('department_name')
        department, _ = Department.objects.get_or_create(name=department_name)
        doctor, created = Doctor.objects.get_or_create(
            department=department, user_id=data['user'])
        if created:
            print(f'Doctor {doctor.user.get_full_name()} created.')
        else:
            print(f'Doctor {doctor.user.get_full_name()} already exists.')

    nurses = [
        {'user': 4, 'department_name': 'Cardiology'},
        {'user': 5, 'department_name': 'Neurology'},
    ]

    for data in nurses:
        department_name = data.pop('department_name')
        department, _ = Department.objects.get_or_create(name=department_name)
        nurse, created = Nurse.objects.get_or_create(
            department=department, user_id=data['user'])
        if created:
            print(f'Nurse {nurse.user.get_full_name()} created.')
        else:
            print(f'Nurse {nurse.user.get_full_name()} already exists.')
