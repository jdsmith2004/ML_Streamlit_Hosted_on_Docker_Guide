# Idaho Target Data Visualization App

A Streamlit application that visualizes Idaho Target data with various Plotly charts.

## Dataset

This application requires an `idaho_target.parquet` file in the root directory. The file should contain a column named `total_quantity` which will be used for the visualizations.

## Running the Application

### Option 1: Run with Python directly

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your browser and go to `http://localhost:8501`

### Option 2: Run with Docker

1. Build the Docker image:
   ```bash
   docker build -t idaho-target-viz .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8501:8501 idaho-target-viz
   ```

3. Open your browser and go to `http://localhost:8501`

## Features

This application includes:

- Interactive data filtering
- Various chart types:
  - Bar charts
  - Histograms
  - Pie/donut charts
  - Time series line charts
  - Correlation heatmaps
  - Box plots
  - Bubble charts
- Responsive layout with multiple columns
- Summary statistics

## Docker Compose (Optional)

For easy deployment, you can use Docker Compose:

```yaml
version: '3'
services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./:/app
```

Save this as `docker-compose.yml` and run:
```bash
docker-compose up
```

## Screenshots

*Add screenshots of your application here*