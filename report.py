import pandas as pd
import os

def generate_report():
    base_path = "Attendance"
    all_data = []

    # Loop through all subject folders
    for subject in os.listdir(base_path):
        file_path = os.path.join(base_path, subject, "attendance.csv")

        if os.path.exists(file_path):
            df = pd.read_csv(file_path)

            # Convert wide format → long format
            df_long = df.melt(
                id_vars=["Enrollment", "Name"],
                var_name="Date",
                value_name="Present"
            )

            # Remove unwanted column
            df_long = df_long[df_long["Date"] != "Attendance"]

            # Clean name
            df_long["Name"] = df_long["Name"].astype(str).str.replace(r"[\[\]']", "", regex=True)

            # Add subject
            df_long["Subject"] = subject

            all_data.append(df_long)

    # Combine all subjects
    final_df = pd.concat(all_data)

    # Convert date
    final_df["Date"] = pd.to_datetime(final_df["Date"], errors='coerce')

    # Add Month column
    final_df["Month"] = final_df["Date"].dt.month

    # Filter present
    present_df = final_df[final_df["Present"] == 1]

    # -------- OVERALL --------
    total_days = final_df["Date"].nunique()

    overall = present_df.groupby(
        ["Enrollment", "Name"]
    ).size().reset_index(name="Days")

    overall["Percentage"] = (overall["Days"] / total_days) * 100

    # -------- MONTHLY (FIXED 🔥) --------
    monthly = present_df.groupby(
        ["Enrollment", "Name", "Month", "Subject"]
    ).size().reset_index(name="Days")

    # Total classes per Month + Subject
    total_classes = final_df.groupby(
        ["Month", "Subject"]
    )["Date"].nunique().reset_index(name="TotalClasses")

    # Merge
    monthly = pd.merge(monthly, total_classes, on=["Month", "Subject"])

    # Percentage
    monthly["Percentage"] = (monthly["Days"] / monthly["TotalClasses"]) * 100

    # -------- SUBJECT --------
    subject_df = present_df.groupby(
        ["Enrollment", "Name", "Subject"]
    ).size().reset_index(name="Days")

    return overall, monthly, subject_df