# Encyclopedia Wiki

A Django-based online encyclopedia application that allows users to create, view, edit, and search through encyclopedia entries stored as Markdown files.

## Features

- **Browse Entries**: View all available encyclopedia entries on the home page
- **Search**: Search through entries with real-time matching
- **Create New Pages**: Add new encyclopedia entries using Markdown
- **Edit Existing Pages**: Modify and update existing entries
- **Random Page**: Discover random entries
- **Responsive Design**: Clean, Bootstrap-based interface

## Project Structure

```
wiki/
├── encyclopedia/           # Main Django app
│   ├── migrations/         # Database migrations
│   ├── static/            # Static files (CSS, images)
│   ├── templates/         # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py           # URL routing
│   ├── util.py           # File operations utilities
│   └── views.py          # View functions
├── entries/               # Markdown entry files
├── wiki/                  # Django project settings
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── README.md
```

## Available Entries

The encyclopedia currently includes entries for:
- **CSS** - Cascading Style Sheets
- **Django** - Python web framework
- **Git** - Version control system
- **HTML** - HyperText Markup Language
- **Python** - Programming language

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/abimoussagnes/wiki.git>
   cd wiki
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Open your browser** and navigate to `http://127.0.0.1:8000/`

## Usage

### Viewing Entries
- Visit the home page to see all available entries
- Click on any entry title to view its content
- Use the search bar to find specific entries

### Creating New Entries
1. Click "Create New Page" from the sidebar
2. Enter a title and Markdown content
3. Submit to save the new entry

### Editing Entries
1. Navigate to any existing entry
2. Click the "Edit" link
3. Modify the Markdown content
4. Save changes

### Searching
- Use the search bar in the sidebar
- Results show partial matches
- Exact matches redirect directly to the entry

## Technical Details

- **Framework**: Django 3.0.2
- **Database**: SQLite
- **Frontend**: Bootstrap 4.4.1, Custom CSS
- **Markdown Processing**: markdown2 library
- **File Storage**: Django's default storage system

## API Endpoints

- `/` - Home page (list all entries)
- `/wiki/<title>/` - View specific entry
- `/search/` - Search functionality
- `/new/` - Create new entry form
- `/result/` - Process new entry creation
- `/random/` - Redirect to random entry
- `/wiki/<name>/edit/` - Edit entry form
- `/wiki/<name>/new/` - Process entry updates

## Development

### Adding New Features
1. Create new views in `encyclopedia/views.py`
2. Add URL patterns in `encyclopedia/urls.py`
3. Create corresponding templates in `encyclopedia/templates/encyclopedia/`
4. Update this README with new features

### File Organization
- Entries are stored as `.md` files in the `entries/` directory
- Static files (CSS, images) go in `encyclopedia/static/encyclopedia/`
- Templates use the `encyclopedia/` namespace

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of CS50's Web Programming with Python and JavaScript course.
