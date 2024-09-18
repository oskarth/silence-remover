# Silence Remover

A Python script that removes silent gaps from MP3 files.

## Prerequisites

- Python 3.7+
- FFmpeg:
  - macOS: `brew install ffmpeg`
  - Ubuntu/Debian: `sudo apt-get update && sudo apt-get install ffmpeg`
  - Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add to PATH

## Setup

1. Clone this repository or download `silence_remover.py`, `run_silence_remover.sh`, and `requirements.txt`.
2. Make the shell script executable:
   ```bash
   chmod +x run_silence_remover.sh
   ```

## Usage

Run the script:

```bash
./run_silence_remover.sh input.mp3 output.mp3
```

Optional parameters:
- `--min_silence_len`: Minimum silence length in ms (default: 1000)
- `--silence_thresh`: Silence threshold in dB (default: -50)

Example:
```bash
./run_silence_remover.sh input.mp3 output.mp3 --min_silence_len 500 --silence_thresh -40
```

The script automatically sets up a virtual environment and installs dependencies on first run.

## Troubleshooting

- Ensure Python 3.7+ and FFmpeg are installed and accessible from the terminal.
- If modules are missing, delete the `venv` directory and rerun the script.

## License

MIT License - see the [LICENSE](LICENSE) file for details.