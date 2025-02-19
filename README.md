<div align="center">
  <img src="assets/icons/HHS Hawks.ico" alt="HHS Hawks Icon">
   <h1>Highland Highlights</h1>
   <h3>Connecting Highland through the power of information.</h3>
   <h4>
      <a href="#about">About</a> •
      <a href="#features">Features</a> •
      <a href="#how-to-use">How To Use</a> •
      <a href="#download">Download</a> •
      <a href="#development">Development</a> •
      <a href="#feedback">Feedback</a> •
      <a href="#license">License</a> •
      <a href="#author">Author</a> •
      <a href="#contact">Contact</a>
   </h4>
</div>

## About

*Highland Highlights* is a modern, dynamic digital bulletin board application I made as a student at Highland, for Highland. Built for Windows using the *Qt for Python* framework, it was designed to replace the old, outdated TV info system with a cleaner look and feel, together along with additional features to better serve the needs of our community.

## Features

- **Clock & Date**: View the time and date.
- **Weather**: Display the current local weather conditions.
- **Weekly Announcements**: Present weekly announcements as scrolling text, easily updated from a DOCX file.
- **Club Advertisements Slideshow**: Showcase club events, promotions, and news in a slideshow format. Keep students informed about extracurricular activities by directly importing it as a PDF document.

## [Download](https://github.com/jack-baril/highland-highlights/releases/download/v1.0.0-alpha/highland-highlights.zip)

Download *Highland Highlights* with the embedded link above. Once highland-highlights.zip is downloaded, unzip it. Then, refer to the [How To Use](#how-to-use) section for instructions on how to use the application.

## How To Use

1. Prepare your weekly announcements within a DOCX file and create a slideshow in your software of choice with the dimensions 1920x910px for the club advertisements. Each club advertisement should be placed on a separate page in the PDF document.

2. Put both your DOCX file and the PDF document into the "uploads" folder.

3. Open Highland Highlights.exe. You may get a warning message from Windows Security; click More info, then Run anyway.

> [!NOTE]  
> To make changes to the content in the scrolling weekly announcements or the club advertisements slideshow, simply insert copies of your new DOCX file and PDF document into the "uploads" folder. The application will update the contents with your new imports automatically without a restart.

## Development

To modify *Highland Highlights*, refer to the steps in this section. **Technical knowledge is required.**

### Prerequisites

- Python 3.12+
- Git

### Installation

1. Clone the GitHub repository and navigate to the project directory:

   ```sh
   git clone https://github.com/jack-baril/highland-highlights.git
   cd highland-highlights
   ```

2. Set up a virtual environment (optional but highly recommended):

   Setup procedures differ based on your terminal's shell and operating system. For instructions on creating a virtual environment on your local machine, please refer to the [official documentation](https://docs.python.org/3/library/venv.html).

3. Install the necessary packages and dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Create an account and get a free API key from [WeatherAPI](https://www.weatherapi.com).

5. Enter your API key in [config.py](app/config.py) into the quotation marks within the appropriate line (shown below):

   ```python
   API_KEY = ""
   ```

### Configuration

To configure the application, you can modify the constants in the following files:

| File                             | Description                        | 
| -------------------------------- | ---------------------------------- |
| [styles.py](app/theme/styles.py) | Controls the appearance of widgets |
| [config.py](app/config.py)       | Contains application settings      |

### Build

1. To save your configurations, use the following command to generate the executable file:

   ```sh
   pyinstaller app/main.py --exclude-module=PySide6_Addons --exclude-module=PySide6_Essentials --icon="assets/icons/HHS Hawks.ico" --name="Highland Highlights"  --noconsole --onefile
   ```

2. You will find the executable file inside the "dist" folder.

> [!NOTE]  
> If you wish to save any additional changes, re-generate the executable file. However, this time run:
>
> ```sh
> pyinstaller "Highland Highlights.spec"
> ```
>
> You might need to temporarily disable Real-time protection in the Virus & threat protection settings of Windows Security to allow pyinstaller to complete its tasks successfully.

## Feedback

Please give me feedback by [emailing me](#contact). If you have any problems with *Highland Highlights*, please submit an issue to [my GitHub repository](https://github.com/jack-baril/highland-highlights/issues).

## License

Distributed under the [MIT License](LICENSE.txt).

## Author

<a href="https://github.com/jack-baril/highland-highlights/graphs/contributors">
   <img src="https://contrib.rocks/image?repo=jack-baril/highland-highlights" />
</a>

## Contact

Email: [jack.r.baril@gmail.com](mailto:jack.r.baril@gmail.com)
