import aspose.diagram
from aspose.diagram import *
import random
import spacy

# Load the English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Prompt the user for a sentence
sentence = input("Please enter a sentence: ")

# Process the sentence using spaCy
doc = nlp(sentence)

# Load stencil file
diagram = Diagram("C:\\Users\\Public\\Stencil3.vssx")

# Function to add a shape with text
def add_shape(page, text, x, y, width, height, shape_type="Circle"):

    shape_id = diagram.add_shape(x, y, width, height, shape_type, 0)
    shape = page.shapes.get_shape(shape_id)
    shape.text.value.add(aspose.diagram.Txt(text))
    return shape_id

# Calculate the layout of the shapes
x_offset = 0.5  # Horizontal space between shapes
y_offset = 1.0  # Vertical space between levels
shape_width = 1.5
shape_height = 0.5

# Create a mapping from tokens to shape IDs and positions
token_shape_map = {}
positions = {}

# Determine the position for each token
for index, token in enumerate(doc):
    # x = x_offset + (index * (shape_width + x_offset))
    x = x_offset + random.random() * 5
    # y = 5.5  # Starting y position
    y = 5.5 + random.random() * 5
    positions[token] = (x, y)

# Add shapes for each token
for token in doc:
    x, y = positions[token]
    shape_id = add_shape(diagram.pages[0], token.text, x, y, shape_width, shape_height)
    token_shape_map[token] = shape_id

# Add connectors for each dependency
for token in doc:
    if token.head != token:
        head_x, head_y = positions[token.head]
        child_x, child_y = positions[token]
        diagram.pages[0].connect_shapes_via_connector(
            token_shape_map[token.head], ConnectionPointPlace.CENTER,
            token_shape_map[token], ConnectionPointPlace.CENTER)




# Save as VSDX
diagram.save("C:\\Users\\Public\\dependency_tree.vsdx", SaveFileFormat.VSDX)
