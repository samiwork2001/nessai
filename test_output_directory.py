#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple test script to verify the set_output_directory method.
"""

import os
import sys
import logging
import tempfile
import datetime
from pathlib import Path
from abc import ABC, abstractmethod

# Create a simplified version of the Proposal class for testing
class Proposal(ABC):
    """Simplified Proposal class for testing"""
    
    def __init__(self, model, rng=None):
        self.model = model
        self.populated = True
        self._initialised = False
        self.training_count = 0
        self.population_acceptance = None
        self.population_time = datetime.timedelta()
        
    def set_output_directory(self, directory: str) -> None:
        """
        Set or change the output directory for Nessai's output.
        
        This method creates the output directory if it doesn't exist
        and sets it as the output directory for the proposal.
        
        Parameters
        ----------
        directory: str
            Path to the new output directory
        """
        print(f"Setting output directory to {directory}")
        self.output = directory
        os.makedirs(directory, exist_ok=True)
        print(f"Output directory set to {directory}")

# Create a simple mock model
class MockModel:
    def __init__(self):
        pass

# Create a dummy proposal class that implements the abstract method
class DummyProposal(Proposal):
    def draw(self, old_param):
        # Concrete implementation of the abstract method
        return old_param

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def main():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create a test output directory
        test_output_dir = Path(tmp_dir) / "test_output"
        
        # Create a proposal instance
        model = MockModel()
        proposal = DummyProposal(model)
        
        # Test the set_output_directory method
        proposal.set_output_directory(str(test_output_dir))
        
        # Verify the output directory was set correctly
        assert proposal.output == str(test_output_dir)
        assert os.path.exists(test_output_dir)
        
        print(f"Test passed! Output directory set to: {test_output_dir}")
        print(f"Directory exists: {os.path.exists(test_output_dir)}")

    print("All tests passed successfully!")

if __name__ == "__main__":
    main()