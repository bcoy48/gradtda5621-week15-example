import os
from Bio import File
from Bio import SeqIO

def parse_annotated_bio_file(file_location):

  # Instantiate two lists to write the parsed sentences to
  main_phrases = []
  temp_tokens = []

  # Open the first file to understand the contents
  with File.as_handle(file_location, 'r') as f:

      # Parse the annotated text (e.g., word\t<annotation>\n)
      for record in SeqIO.parse(f, 'tab'):

        # Check if the end of a phrase has been reached
        # identified by a comma or period
        if record.id.strip() == '.':

          # Convert the tokens to a common English phrase
          main_phrases.append(' '.join(temp_tokens) + '.')

          # Reset the list of phrase tokens
          temp_tokens = []

        else:
          # Append the phrasetoken
          temp_tokens.append(record.id)

  # Close the open file
  f.close()

  # Return the final list of phrases
  return main_phrases
