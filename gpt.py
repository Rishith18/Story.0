# importing required modules
from pypdf import PdfReader
from openai import OpenAI

def scrape_pages(pdf):
    # creating a pdf reader object
    reader = PdfReader(pdf)
    
    # initializing an array to store text from each page
    pages_text = []

    # iterating through each page and extracting text
    for page in reader.pages:
        text = page.extract_text()
        if text:  # ensure only non-empty text is appended
            pages_text.append(text)

    # printing number of pages and returning the array
    print(f"Number of pages: {len(pages_text)}")
    return pages_text

def simplify_text(text):
    client = OpenAI(
        api_key="sk-J3WRn5WLFwz0mMg-9CaggQ", # set this!!!
        base_url="https://nova-litellm-proxy.onrender.com" # and this!!!
    )
    
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"""Break down this text into 15 large chunks where each chunk provides relavent information to the story. 
                                                Start the first chunk where the story begins and end the last chunk when the story ends which will be close to the last page of the book.
                                                Generate prompts of these chunks for a Dalle-E image generation prompt where the images will be used to create a picture book.
                                                The prompts should include many descriptive details that allow the Dalle-E image generation model to provide the images for the book.
                                                Make the prompt that will become a picture for a child ages 7-10 by dumbing down complex topics and prompting the image for a cartoon style.
                                                Make the prompt detailed and ensure that each prompt flows with the next for pictures that will flow with each other.
                                                Make each prompt atleast 2 sentences to provide ample detail for Dalle-E
                                                List these prompts without bullet points or numbersby leaving a space inbetween each prompt

                                                These prompts should be in a similar format and as descriptive as this example: 
                                                a cat floating in a body of water with blue water, in the style of holographic, light pink and light aquamarine, brightly colored, luminous fantasies, hyper-realistic water

                                                Here is another example to refer to:
                                                aper craft image of an excited adult monkey swinging from a branch in a tree. Hyperactive. Energetic. Paper art. Paper craft. 
                                                Intricate paper shapes. Layers of detailed paper design. 3D extruded design. Color palette of grayscale with flashes of yellow as accents.

                                                Here is another example to refer to:
                                                An anthropomorphic blueberry waiter, viewed from the side, stands in an old cafe setting; a grumpy expression on his face, a slightly hunched posture that 
                                                emphasizes his age. The blueberry character has realistic textured skin with subtle wrinkles. He wears a multi-layered waiter's uniform: a white shirt with 
                                                rolled-up sleeves, an old-fashioned black vest, and a slightly stained apron tied around the waist. One hand holds a tray with a cup of steaming coffee, and 
                                                the other adjusts a small bow tie. In the background are tables and chairs, dim ambient lighting. Cinematic focus on the character's intense eyes and expressive, 
                                                annoyed look, detailed textures and warm colors

                                                Each prompt should ALWAYS include a sentence describing every character or person in the prompt with great detail, each prompt should describe the face, body, and clothing of each character or person. 
                                                Each description of the character or person should be same in every prompt generated.

                                                Write "Cartoonish style, with color, " in each prompt. 
                                                
                                                Here is the text you must chunk and make into prompts, summarize the 15 chunks into 15 one sentence summaries each in simple language that an 8 year old can understand and print these first, 
                                                then under these summaries print 15 the prompts. Do not print any headers, only print the summaries and prompts and nothing else with space inbetween in summary and prompt. 
                                                Write "SUMMARIES" before the summaries and "PROMPTS" before the prompts:\n\n{text}"""
                                                }],
        stream=True,
    )
    full_story = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            full_story = full_story + chunk.choices[0].delta.content
    return full_story

def store_all_pages_text(pages):
    all_text = ""
    for i, page_text in enumerate(pages):
        # Append each page's content in the required format
        all_text += f"--- Page {i + 1} ---\n" + page_text + "\n\n"
    return all_text

# Generates two arrays, one holds all captions (summaries) and other holds all prompts (promptss)
def create_prompts_summaries(pdf):
    all_pages_text = scrape_pages(pdf)
    all_text = store_all_pages_text(all_pages_text)

    prompts = simplify_text(all_text)
    print(prompts) # Debug statement

    prompts = prompts.splitlines()

    cleaned_prompts = list(filter(lambda x: x != "", prompts))

    summaries = cleaned_prompts[1:cleaned_prompts.index("PROMPTS")]
    promptss = cleaned_prompts[cleaned_prompts.index("PROMPTS") + 1:]
    
    return summaries, promptss
    