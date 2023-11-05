from bs4 import BeautifulSoup

html_code = """
<div className="flex flex-col min-h-screen bg-gray-200 p-4 md:p-0">
  <main className="flex flex-col items-center justify-center w-full">
    <section className="max-w-3xl w-full mt-16 grid grid-cols-1 md:grid-cols-1 gap-4">
    </section>
  </main>
</div>


you can add your code
"""

# Parse the HTML code
soup = BeautifulSoup(html_code, 'html.parser')

# Find all elements with a className attribute
elements_with_class = soup.find_all(attrs={"classname": True})

# Remove the className attribute from each element
for element in elements_with_class:
    del element['classname']

# Print the modified HTML
print(soup.prettify())
