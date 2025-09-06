# WebP Image Compressor

A fast and efficient Python script to convert and compress images to **WebP** format while preserving transparency. This tool supports multiple image formats and processes images concurrently for optimal performance.

## Features

* Converts images to WebP format.
* Maintains transparency for PNGs and palette-based images.
* Supports popular image formats: JPG, JPEG, PNG, BMP, TIFF, GIF.
* Batch processing with folder recursion.
* Concurrent processing using multiple threads for faster conversion.
* Outputs compressed images in a separate folder structure.

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/webp-image-compressor.git
cd webp-image-compressor
```

2. **Install dependencies**:

```bash
pip install pillow
```

> `Pillow` is the Python Imaging Library (PIL) fork used to handle image processing.

## Usage

Run the script from the command line:

```bash
python main.py <input_folder> <quality>
```

* `<input_folder>`: Path to the folder containing images to compress.
* `<quality>`: Compression quality from 0 (lowest) to 100 (highest).

**Example:**

```bash
python main.py ./images 80
```

This will compress all supported images in `./images` and save them in `./images/output_webp` while keeping the folder structure.

## Supported Formats

* JPEG / JPG
* PNG
* BMP
* TIFF
* GIF

## Notes

* Images with transparency are converted to WebP with alpha channel preserved.
* Non-RGB images are automatically converted to RGB for compatibility.
* Output images are stored in a folder named `output_webp` inside the input folder.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you encounter bugs or have suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

