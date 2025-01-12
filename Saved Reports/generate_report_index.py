import os

# Define the root directory where student folders are located
root_folder = "PA1"

# Start building the top-level index.html content
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>MOSS Reports - PA1</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #0056b3;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 20px 0;
            box-sizing: border-box;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #0056b3;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        a {
            text-decoration: none;
            color: #007BFF;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    <script>
        function filterTable() {
            const input = document.getElementById("searchBar").value.toLowerCase();
            const rows = document.querySelectorAll("#reportTable tbody tr");
            rows.forEach(row => {
                const name = row.querySelector("td:nth-child(2)").textContent.toLowerCase();
                row.style.display = name.includes(input) ? "" : "none";
            });
        }
    </script>
</head>
<body>
    <h1>MOSS Reports for PA1</h1>
    <p>Search for a student's CruzID:</p>
    <input type="text" id="searchBar" placeholder="Type to search..." onkeyup="filterTable()">
    <table id="reportTable">
        <thead>
            <tr>
                <th>#</th>
                <th>Student Name</th>
                <th>Report Link</th>
            </tr>
        </thead>
        <tbody>
"""

# Loop through student folders, add serial numbers, and find the correct .html file inside
serial_no = 1
for student_folder in sorted(os.listdir(root_folder)):
    student_path = os.path.join(root_folder, student_folder)
    if os.path.isdir(student_path):  # Ensure it's a folder
        # Find the .html file inside the student's folder
        for file in os.listdir(student_path):
            if file.endswith(".html") and file.startswith("Matches"):
                # Add a serial number and link to the .html file
                html_content += f"""            <tr>
                <td>{serial_no}</td>
                <td>{student_folder}</td>
                <td><a href="./{student_folder}/{file}">View Report</a></td>
            </tr>\n"""
                serial_no += 1
                break

# Close the HTML structure
html_content += """        </tbody>
    </table>
</body>
</html>
"""

# Write the content to the top-level index.html
with open(os.path.join(root_folder, "index.html"), "w") as f:
    f.write(html_content)

print("Top-level index.html with search and CSS styling generated successfully!")

