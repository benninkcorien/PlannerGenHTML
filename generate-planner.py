from jinja2 import Environment, FileSystemLoader

# Set up Jinja environment
env = Environment(
    loader=FileSystemLoader("F:\\PlannerGenerator\\PlannerGenHTML\\html\\")
)

# Get the base template
template = env.get_template("planner_full.html")

# Render the template (you can pass variables if needed)
rendered_html = template.render()

# Save the rendered HTML to a file
with open(
    r"F:\PlannerGenerator\PlannerGenHTML\html\planner_full_result.html",
    "w",
    encoding="utf-8",
) as file:
    file.write(rendered_html)
