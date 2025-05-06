def format_job_data(job_data):
    """
    Cleans and formats raw job data list.
    Assumes each item is a dictionary with at least 'title' and 'company'.
    Removes duplicates and strips extra whitespace.
    """
    seen = set()
    formatted = []

    for job in job_data:
        title = job.get("title", "").strip()
        company = job.get("company", "").strip()

        # Skip incomplete records
        if not title or not company:
            continue

        # Avoid duplicates based on title + company
        key = f"{title.lower()}_{company.lower()}"
        if key not in seen:
            formatted.append({"title": title, "company": company})
            seen.add(key)

    return formatted
