# l1_template_starter_code

## Description
This repository contains the **starter code** for the *Jinja2 Welcome Page* assignment.  
It provides a simple, styled HTML template that can be adapted to greet a user and display a message such as the time of day.

---

## What’s Inside
- **`index.html`** – A self-contained HTML file with:
  - Clean, modern styling (gradient background, centered layout, large text).  
  - Placeholder greeting and time message that can be customized or dynamically inserted using Jinja2.  

---

## Purpose
The goal of this starter code is to give you a foundation for experimenting with:
- Basic HTML structure.  
- Inline CSS styling.  
- Using **Jinja2 template variables** to replace placeholders (e.g., greeting, username, time).  

---

## How to Use
1. Clone or download this repository.  
2. Open `index.html` in your browser to see the static version.  
3. Replace placeholder text with Jinja2 template variables, for example:  

   ```html
   <h1>Welcome, {{ user_name }}!</h1>
   <p>{{ greeting_message }}</p>
   <p>The time is: {{ current_time }}</p>
4. Consider the use of conditionals for time of day and greeting.
