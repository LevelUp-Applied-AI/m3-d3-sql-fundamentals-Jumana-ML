import sqlite3
def top_departments(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
        SELECT departments.name, SUM(employees.salary) as total_salary
        FROM departments
        JOIN employees ON departments.dept_id = employees.dept_id
        GROUP BY departments.name
        ORDER BY total_salary DESC
        LIMIT 3;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def employees_with_projects(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
        SELECT employees.name, projects.name
        FROM employees
        JOIN project_assignments ON employees.emp_id = project_assignments.emp_id
        JOIN projects ON project_assignments.project_id = projects.project_id;
    """

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def salary_rank_by_department(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
        SELECT employees.name, departments.name, employees.salary,
               RANK() OVER(PARTITION BY employees.dept_id ORDER BY employees.salary DESC) as rank
        FROM employees
        JOIN departments ON employees.dept_id = departments.dept_id
        ORDER BY departments.name ASC, rank ASC;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# This code is to test the functions and print the results to the screen
if __name__ == "__main__":
    # Path to the database file located in the project folder
    db = "drill.db" 
    
    print("--- Task 1: Top Departments ---")
    print(top_departments(db))
    
    print("\n--- Task 2: Employees and Projects ---")
    print(employees_with_projects(db))
    
    print("\n--- Task 3: Salary Rank by Department ---")
    print(salary_rank_by_department(db))