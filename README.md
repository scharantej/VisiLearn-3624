## Flask Application Design

### HTML Files

**index.html**
- Home page for the website, providing an overview of the platform, its features, and how to get started with learning Mandarin using images.
- May include sections for user registration, login, and accessing lessons.

**lessons.html**
- Page displaying a list of all available Mandarin lessons.
- Each lesson should be represented as a link or button leading to the specific lesson page.

**lesson.html**
- Page displaying the content of a Mandarin lesson.
- This page should include an image associated with the lesson's topic and relevant text explaining the concept.
- May also include interactive exercises or quizzes to reinforce learning.

**progress.html**
- Page allowing users to track their progress and set learning goals.
- This page may include charts, graphs, or other visualizations to illustrate the user's progress.

### Routes

**index**
- Route for the home page (`/`).
- Renders the `index.html` file.

**lessons**
- Route for the lessons list page (`/lessons`).
- Renders the `lessons.html` file.

**lesson/<lesson_id>**
- Route for a specific lesson page (`/lesson/1`, `/lesson/2`, etc.).
- Renders the `lesson.html` file with the content of the specified lesson.

**progress**
- Route for the user progress tracking page (`/progress`).
- Renders the `progress.html` file.

**login**
- Route for user login (`/login`).
- Handles user authentication and redirects to the home page upon successful login.

**register**
- Route for user registration (`/register`).
- Handles user registration and redirects to the login page after successful registration.