"""File handling utilities"""
from pathlib import Path
from typing import List, Tuple
import os

class FileHandler:
    @staticmethod
    def get_log_files(directory: str, file_limit: int = 5) -> List[Path]:
        """Get log files from directory, sorted by modification time (newest first)"""
        log_dir = Path(directory)
        
        if not log_dir.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")
        
        # Find all .log and .txt files
        log_files = list(log_dir.glob("*.log")) + list(log_dir.glob("*.txt"))
        
        # Sort by modification time (newest first)
        log_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        
        # Limit results
        return log_files[:file_limit]

    @staticmethod
    def read_file(file_path: str, lines: int = 100) -> List[str]:
        """Read last N lines from file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                all_lines = f.readlines()
            
            # Get last N lines
            return all_lines[-lines:] if len(all_lines) > lines else all_lines
        except Exception as e:
            raise IOError(f"Error reading file {file_path}: {str(e)}")

    @staticmethod
    def write_file(file_path: str, content: List[str]) -> bool:
        """Write content to file"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(content)
            return True
        except Exception as e:
            raise IOError(f"Error writing file {file_path}: {str(e)}")

    @staticmethod
    def read_all_lines(file_path: str) -> List[str]:
        """Read all lines from file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.readlines()
        except Exception as e:
            raise IOError(f"Error reading file {file_path}: {str(e)}")
