# Silence Remover

A Python script that removes silent gaps from MP3 files or folders containing MP3 files.

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

### Processing a single file

```bash
./run_silence_remover.sh input.mp3 output.mp3
```

### Processing a folder of MP3 files

```bash
./run_silence_remover.sh input_folder/ output_folder/
```

### Optional parameters

- `--min_silence_len`: Minimum length of silence (in ms) to be removed (default: 1000)
- `--silence_thresh`: Silence threshold in dB (default: -50)

Example with optional parameters:
```bash
./run_silence_remover.sh input.mp3 output.mp3 --min_silence_len 500 --silence_thresh -40
```

## Making the script globally accessible

To run the script from any directory, add this line to your `~/.zshrc` or `~/.bashrc`:

```bash
alias silence-remover='/path/to/your/run_silence_remover.sh'
```

Replace `/path/to/your/` with the actual path to the script. Then reload your shell configuration:

```bash
source ~/.zshrc  # or ~/.bashrc
```

Now you can use `silence-remover` from any directory:

```bash
silence-remover input.mp3 output.mp3
```

or

```bash
silence-remover input_folder/ output_folder/
```

## Troubleshooting

- Ensure Python 3.7+ and FFmpeg are installed and accessible from the terminal.
- If modules are missing, delete the `venv` directory and rerun the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.