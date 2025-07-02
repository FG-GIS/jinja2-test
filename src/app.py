from jinja2 import Environment, FileSystemLoader
import os
import shutil

# Set up Jinja2 environment to look for templates in the current directory
# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(loader=FileSystemLoader("templates")) # Assuming menu.html is in the same folder

# Load your template
template = env.get_template('menu_template.jinja')

# Your test data (as discussed)
cocktails = [
    {'name': 'Classic Negroni', 'price': 12.00},
    {'name': 'Espresso Martini', 'price': 11.50},
    {'name': 'Daiquiri (Classic)', 'price': 10.00},
]
beers = [
    {'name': 'Peroni Nastro Azzurro', 'price': 5.00},
    {'name': 'Menabrea Original', 'price': 6.50},
]
non_alcoholic_drinks = [
    {'name': 'San Pellegrino Sparkling Water', 'price': 3.50},
    {'name': 'Fresh Lemonade', 'price': 4.50},
]

nome = "Cinci Bar"

# Render the template with the data
rendered_html = template.render(
    bar_name = nome,
    cocktails=cocktails,
    birre=beers,
    analcolici=non_alcoholic_drinks
)

# Save the rendered HTML to a file in the 'public' subdirectory
# Copy the stylesheet from static/menu.css to public/menu.css
shutil.copyfile(os.path.join('static', 'menu.css'), os.path.join('public', 'menu.css'))
os.makedirs('public', exist_ok=True)
with open(os.path.join('public', 'index.html'), 'w') as f:
    f.write(rendered_html)

print("Static HTML menu generated successfully as static_menu.html")