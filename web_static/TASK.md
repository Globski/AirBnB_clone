# Tasks

# Task 0: Inline Styling

Write an HTML page that displays a header and a footer.

### Layout:

**Body:**  
- no margin  
- no padding  

**Header:**  
- color: #FF0000 (red)  
- height: 70px  
- width: 100%  

**Footer:**  
- color: #00FF00 (green)  
- height: 60px  
- width: 100%  
- text: "Best School" center vertically and horizontally  
- always at the bottom of the page  

### Requirements:

- You must use the `<header>` and `<footer>` tags.  
- You are not allowed to import any files.  
- You are not allowed to use the `<style>` tag in the `<head>` tag.  
- Use inline styling for all your tags.

<img width="2160" alt="98f4ac1b0644512ce7ae91a9e8e61e8fe174911d" src="https://github.com/user-attachments/assets/4be5cf19-974b-45d2-86c3-46dcdf6309cf">

**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static
- File: 0-index.html

---

# Task 1: Head Styling

Write an HTML page that displays a header and a footer by using the `<style>` tag in the `<head>` tag (same as 0-index.html).

### Requirements:

- You must use the `<header>` and `<footer>` tags.  
- You are not allowed to import any files.  
- No inline styling.  
- You must use the `<style>` tag in the `<head>` tag.  
- The layout must be exactly the same as 0-index.html.

**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: 1-index.html

---

# Task 2: CSS Files

Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html).

### Requirements:

- You must use the `<header>` and `<footer>` tags.  
- No inline styling.  
- You must have **3 CSS files**:
  - `styles/2-common.css`: for global style (i.e. the body style)
  - `styles/2-header.css`: for header style
  - `styles/2-footer.css`: for footer style
- The layout must be exactly the same as 1-index.html.

**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: 2-index.html, `styles/2-common.css`, `styles/2-header.css`, `styles/2-footer.css`

---

# Task 3: Zoning Done!

Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html).

### Layout:

**Common:**
- No margin  
- No padding  
- Font color: #484848  
- Font size: 14px  
- Font family: Circular, "Helvetica Neue", Helvetica, Arial, sans-serif  
- Icon in the browser tab  

**Header:**
- Color: white  
- Height: 70px  
- Width: 100%  
- Border bottom: 1px solid #CCCCCC  
- Logo aligned to the left and centered vertically (20px space at the left)  

**Footer:**
- Color: white  
- Height: 60px  
- Width: 100%  
- Border top: 1px solid #CCCCCC  
- Text: "Best School" centered vertically and horizontally  
- Always at the bottom of the page  

### Requirements:

- No inline styles  
- You are not allowed to use the `<img>` tag  
- You are not allowed to use the `<style>` tag in the `<head>` tag  
- All images must be stored in the `images` folder  
- You must have **3 CSS files**:
  - `styles/3-common.css`: for the global style (i.e. body style)
  - `styles/3-header.css`: for the header style
  - `styles/3-footer.css`: for the footer style

<img width="2160" alt="2be1eda05a0d9097c210f2d3482a59aa858c5711 (1)" src="https://github.com/user-attachments/assets/82ae1bf5-17e2-4b3b-b629-f7a80693a36c">

**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: 3-index.html, `styles/3-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `images/`

---

# Task 4: Search!

Write an HTML page that displays a header, footer, and a filters box with a search button.

### Layout: (based on 3-index.html)

**Container:**
- Between `<header>` and `<footer>` tags, add a `<div>`:
  - `class="container"`
  - Max width: 1000px
  - Margin top and bottom: 30px (it should be 30px under the bottom of the header)
  - Center horizontally  

**Filter Section:**
- `<section>` tag
  - `class="filters"`
  - Inside the `.container`
  - Color: white
  - Height: 70px
  - Width: 100% of the container
  - Border: 1px solid #DDDDDD with radius 4px  

**Search Button:**
- `<button>` tag
  - Text: "Search"
  - Font size: 18px
  - Inside the `.filters` section
  - Background color: #FF5A5F
  - Text color: #FFFFFF
  - Height: 48px
  - Width: 20% of the `.filters` section
  - No borders
  - Border radius: 4px
  - Center vertically and 30px from the right border
  - Change opacity to 90% when the mouse hovers over the button  

### Requirements:

- You must use: `<header>`, `<footer>`, `<section>`, and `<button>` tags  
- No inline styles  
- You are not allowed to use the `<img>` tag  
- You are not allowed to use the `<style>` tag in the `<head>` tag  
- All images must be stored in the `images` folder  
- You must have **4 CSS files**:
  - `styles/4-common.css`: for the global style (body and `.container` styles)
  - `styles/3-header.css`: for the header style
  - `styles/3-footer.css`: for the footer style
  - `styles/4-filters.css`: for the filters style

**Note:**  
- `4-index.html` won’t be W3C valid, don’t worry, it’s temporary.

<img width="2160" alt="f959154b0cdf1cdf71ddef04e3787ef28462793e" src="https://github.com/user-attachments/assets/c4bd02cf-1cbe-4b53-a46e-c8cd1e15dd4b">


**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: 4-index.html, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/4-filters.css`, `images/`

---

# Task 5: More Filters

Write an HTML page that displays a header, footer, and a filters box.

### Layout: (based on 4-index.html)

**Locations and Amenities Filters:**
- `<div>` tags
  - `class="locations"` for the location filter and `class="amenities"` for the amenities filter  
  - Inside the `.filters` section (same level as the "Search" button)
  - Height: 100% of the `.filters` section
  - Width: 25% of the `.filters` section
  - Border-right: 1px solid #DDDDDD (only for the first left filter, i.e., location filter)
  
  **Contains a Title:**
  - `<h3>` tag
    - Font weight: 600
    - Text: "States" for location filter or "Amenities" for the amenities filter

  **Contains a Subtitle:**
  - `<h4>` tag
    - Font weight: 400
    - Font size: 14px
    - Text: fake contents (e.g., list of states or amenities)

### Requirements:

- You must use: `<header>`, `<footer>`, `<section>`, `<button>`, `<h3>`, and `<h4>` tags  
- No inline styles  
- You are not allowed to use the `<img>` tag  
- You are not allowed to use the `<style>` tag in the `<head>` tag  
- All images must be stored in the `images` folder  
- You must have **4 CSS files**:
  - `styles/4-common.css`: for the global style (body and `.container` styles)
  - `styles/3-header.css`: for the header style
  - `styles/3-footer.css`: for the footer style
  - `styles/5-filters.css`: for the filters style

<img width="2160" alt="85bfa50b96c2985723daa75b5e22f75ef16e2b2e" src="https://github.com/user-attachments/assets/69ecf449-d21a-43a0-9ee0-3f3cd093b42e">


**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: 5-index.html, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/5-filters.css`, `images/`

---

# Task 6: It's (h)over

Write an HTML page that displays a header, footer, and a filters box with dropdown.

### Layout: (based on 5-index.html)

**Update Locations and Amenities Filters to Display a Contextual Dropdown:**

- **Tag:** `<ul>`
  - `class="popover"`
  - Text should be fake for now
  - Inside each filter `<div>`
  - **Not displayed by default**
  - Background color: #FAFAFA
  - Width: same as the div filter
  - Border: 1px solid #DDDDDD with border-radius: 4px
  - No list-style display
  
- **Location Filter has 2 levels of `<ul>`/`<li>`:**
  - State -> Cities
  - The state name should be displayed in an `<h2>` tag with font size 16px

### Requirements:

- You must use: `<header>`, `<footer>`, `<section>`, `<button>`, `<h3>`, `<h4>`, `<ul>`, and `<li>` tags  
- No inline styles  
- You are not allowed to use the `<img>` tag  
- You are not allowed to use the `<style>` tag in the `<head>` tag  
- All images must be stored in the `images` folder  
- You must have **4 CSS files**:
  - `styles/4-common.css`: for the global style (body and `.container` styles)
  - `styles/3-header.css`: for the header style
  - `styles/3-footer.css`: for the footer style
  - `styles/6-filters.css`: for the filters style

<img width="2160" alt="6262f13624dca23ca19db505c44f88faddb82ebb" src="https://github.com/user-attachments/assets/a3e10fdc-04b6-49ec-b7fe-07d41d9614f5">

<img width="2160" alt="6e6bdfa13fa88a5f439d9e2b1dade826dd95529b" src="https://github.com/user-attachments/assets/327ecbac-78a1-48e6-9838-cffb8baa6672">


**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: 6-index.html, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/6-filters.css`, `images/`

---

# Task 7: Display Results

Write an HTML page that displays a header, footer, a filters box with dropdown, and results.

### Layout: (based on 6-index.html)

**Add Places Section:**
- Tag: `<section>`
  - `class="places"`
  - Same level as the filters section, inside `.container`

**Contains a Title:**
- Tag: `<h1>`
  - Text: "Places"
  - Align in the top left
  - Font size: 30px

**Contains Multiple “Places” as Listings (horizontal or vertical):**
- Tag: `<article>`
  - Width: 390px
  - Padding and margin: 20px
  - Border: 1px solid #FF5A5F with border-radius: 4px

**Contains the Place Name:**
- Tag: `<h2>`
  - Font size: 30px
  - Center horizontally

### Requirements:

- You must use: `<header>`, `<footer>`, `<section>`, `<article>`, `<button>`, `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<ul>`, and `<li>` tags  
- No inline styles  
- You are not allowed to use the `<img>` tag  
- You are not allowed to use the `<style>` tag in the `<head>` tag  
- All images must be stored in the `images` folder  
- You must have **5 CSS files**:
  - `styles/4-common.css`: for the global style (i.e. body and `.container` styles)
  - `styles/3-header.css`: for the header style
  - `styles/3-footer.css`: for the footer style
  - `styles/6-filters.css`: for the filters style
  - `styles/7-places.css`: for the places style

<img width="2160" alt="bca4d17fbe21a58b66a9d5d6b85df4801d147dd0" src="https://github.com/user-attachments/assets/2db87fce-b34d-4f42-937c-619b9730fcaa">


**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: 7-index.html, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/6-filters.css`, `styles/7-places.css`, `images/`

---

# Task 8: More Details

Write an HTML page that displays a header, a footer, a filter box (dropdown list), and the result of the search.

### Layout: (based on 7-index.html)

**Add More Information to a Place Article:**

1. **Price by Night:**
   - Tag: `<div>`
   - `class="price_by_night"`
   - Same level as the place name (`<h2>`)
   - Font color: #FF5A5F
   - Border: 4px solid #FF5A5F with rounded corners
   - Minimum width: 60px
   - Height: 60px
   - Font size: 30px
   - Align: top right (with space)

2. **Information Section:**
   - Tag: `<div>`
   - `class="information"`
   - Height: 80px
   - Border: top and bottom 1px solid #DDDDDD
   - Contains (align vertically):
   
     - **Number of Guests:**
       - Tag: `<div>`
       - `class="max_guest"`
       - Width: 100px
       - Fake text
       - Icon

     - **Number of Bedrooms:**
       - Tag: `<div>`
       - `class="number_rooms"`
       - Width: 100px
       - Fake text
       - Icon

     - **Number of Bathrooms:**
       - Tag: `<div>`
       - `class="number_bathrooms"`
       - Width: 100px
       - Fake text
       - Icon

3. **User Section:**
   - Tag: `<div>`
   - `class="user"`
   - Text: "Owner: <fake text>"
   - Owner text should be in bold

4. **Description Section:**
   - Tag: `<div>`
   - `class="description"`

### Requirements:

- You must use: `<header>`, `<footer>`, `<section>`, `<article>`, `<button>`, `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<ul>`, and `<li>` tags  
- No inline styles  
- You are not allowed to use the `<img>` tag  
- You are not allowed to use the `<style>` tag in the `<head>` tag  
- All images must be stored in the `images` folder  
- You must have **5 CSS files**:
  - `styles/4-common.css`: for the global style (i.e. body and `.container` styles)
  - `styles/3-header.css`: for the header style
  - `styles/3-footer.css`: for the footer style
  - `styles/6-filters.css`: for the filters style
  - `styles/8-places.css`: for the places style

<img width="1604" alt="f4b2d4ef94bd3a2e7e1ddefa81236595686d270e" src="https://github.com/user-attachments/assets/7bb259fc-5b51-4604-b69f-f3a6c6d138b5">


**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: 8-index.html, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/6-filters.css`, `styles/8-places.css`, `images/`

---

# Task 9: Full Details

Write an HTML page that displays a header, footer, a filters box with dropdown, and results.

### Layout: (based on 8-index.html)

**Add More Information to a Place Article:**

1. **List of Amenities:**
   - Tag: `<div>`
   - `class="amenities"`
   - Margin top: 40px
   - Contains:
   
     - **Title:**
       - Tag: `<h2>`
       - Text: "Amenities"
       - Font size: 16px
       - Border bottom: 1px solid #DDDDDD

     - **List of Amenities:**
       - Tag: `<ul>` / `<li>`
       - No list style
       - Icons on the left (e.g., Pet friendly, TV, Wifi, etc.) — feel free to add more

2. **List of Reviews:**
   - Tag: `<div>`
   - `class="reviews"`
   - Margin top: 40px
   - Contains:
   
     - **Title:**
       - Tag: `<h2>`
       - Text: "Reviews"
       - Font size: 16px
       - Border bottom: 1px solid #DDDDDD

     - **List of Reviews:**
       - Tag: `<ul>` / `<li>`
       - No list style
       
       - A review is described by:
         - `<h3>` tag for the user/date description (font size: 14px). Example: "From Bob Dylan the 27th January 2017"
         - `<p>` tag for the text (font size: 12px)

### Requirements:

- You must use: `<header>`, `<footer>`, `<section>`, `<article>`, `<button>`, `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<ul>`, and `<li>` tags  
- No inline styles  
- You are not allowed to use the `<img>` tag  
- You are not allowed to use the `<style>` tag in the `<head>` tag  
- All images must be stored in the `images` folder  
- You must have **5 CSS files**:
  - `styles/4-common.css`: for the global style (i.e. body and `.container` styles)
  - `styles/3-header.css`: for the header style
  - `styles/3-footer.css`: for the footer style
  - `styles/6-filters.css`: for the filters style
  - `styles/100-places.css`: for the places style

<img width="2160" alt="f54486a431a05ea3477e337e0e953686d3c6ffd0" src="https://github.com/user-attachments/assets/cd9cb241-a962-4f13-970d-1cc99c40457b">


**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: 100-index.html, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/6-filters.css`, `styles/100-places.css`, `images/`

---

# Task 10: Flex

Improve the Places section by using [**Flexible Boxes**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox) for all Place articles.

[**Flexbox Froggy**](https://flexboxfroggy.com/)

### Requirements:

- You must use **Flexbox** to arrange the Place articles in the Places section.
- Ensure that all Place articles are properly aligned using Flexbox properties.

**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: `101-index.html`, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/6-filters.css`, `styles/101-places.css`, `images/`

---

# Task 11: Responsive Design

Improve the page by adding [**responsive design**](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design) to display correctly on mobile or small screens.

### Examples:
- Prevent horizontal scrolling on smaller screens.
- Redesign the search bar depending on the width of the screen.
- Other general responsive design improvements to enhance the page's layout on mobile devices.

**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: `102-index.html`, `styles/102-common.css`, `styles/102-header.css`, `styles/102-footer.css`, `styles/102-filters.css`, `styles/102-places.css`, `images/`

---

# Task 12: Accessibility

Improve the page by adding [**Accessibility**](https://developer.mozilla.org/en-US/docs/Learn/Accessibility) support.

### Examples:
- Ensure proper **color contrast** for readability, particularly for text on colored backgrounds.
- Use appropriate **header tags** (`<h1>`, `<h2>`, etc.) for a clear content hierarchy.
- Consider adding **alt text** for images, appropriate link descriptions, and any other accessibility enhancements for screen readers and keyboard navigation.
- Ensure the page is **navigable** and usable for users with disabilities.

---

**Repo:**

- GitHub repository: AirBnB_clone  
- Directory: web_static  
- File: `103-index.html`, `styles/103-common.css`, `styles/103-header.css`, `styles/103-footer.css`, `styles/103-filters.css`, `styles/103-places.css`, `images/`
