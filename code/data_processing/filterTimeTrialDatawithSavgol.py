import pandas as pd
from scipy.signal import savgol_filter

# Parameters for Savitzky-Golay filter
window_length = 7  # Must be odd and <= number of data points
polyorder = 3

# Load data
input_path = '../../data/prepared_data/preparedTimeTrial.csv'
output_path = '../../data/prepared_data/sg_filtered_4mintt.csv'
df = pd.read_csv(input_path)

# Apply SG filter to each participant column (except 'time')
filtered_df = df.copy()
for col in df.columns:
    if col != 'time':
        # Ensure enough points for the window
        if len(df[col]) >= window_length:
            filtered_df[col] = savgol_filter(df[col], window_length, polyorder)
        else:
            filtered_df[col] = df[col]  # Not enough points, leave unchanged

# Save filtered data
filtered_df.to_csv(output_path, index=False)
print(f"SG-smoothed data saved to {output_path}")