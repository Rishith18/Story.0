import openai
import requests  # Ensure requests library is imported
from pydantic import BaseModel

def outPutGeneration(input_prompts):
    for idx, prompt in enumerate(input_prompts):
        if prompt.strip():  # Check for non-empty prompt
            example_image_generation(prompt, idx)

def example_image_generation(prompt, idx):
    """ 
    Generate an image from the prompt and save it with an index to avoid overwriting.
    """
    client = openai.OpenAI(
        api_key="sk-J3WRn5WLFwz0mMg-9CaggQ",
        base_url="https://nova-litellm-proxy.onrender.com"
    )

    image = client.images.generate(
        prompt=prompt,
        model="dall-e-3",
    )

    print(f"Generated image for paragraph {idx + 1}")
    url = image.data[0].url
    image_path = f"example_image_generation_{idx + 1}.png"
    open(image_path, "wb").write(requests.get(url).content)
    print(f"Image saved as {image_path}")

# Define the input as a list of prompts
input_prompts = ['A cartoon family, the Dursleys, stands proudly outside their house at number four Privet Drive. Mr. Dursley is big and beefy, wearing a gray suit and a large mustache, while Mrs. Dursley is slender, blonde, and has a long neck, peering over their garden fence. Their little son, Dudley, is a round-faced toddler with messy hair, holding a toy. The house is tidy, with a green lawn, and the sky is gray above them. Cartoonish style, with color.', 'Mr. Dursley sits at a breakfast table with a newspaper, while Mrs. Dursley wrestles a screaming Dudley into his high chair. Mr. Dursley wears a plain tie, glasses, and has cereal splatters on his shirt. In the background, a large, tawny owl flies past the window unnoticed. The kitchen is cozy, with a bright sun coming through. Cartoonish style, with color.', 'As Mr. Dursley drives to work, he notices a tabby cat reading a map on the corner of Privet Drive. The cat looks surprisingly wise, with big eyes that seem to understand everything. Mr. Dursley has wide eyes and a puzzled look as he blinks at the strange sight. The street is lined with neat houses and a blue sky above. Cartoonish style, with color.', 'A group of oddly dressed people in colorful cloaks chatter excitedly on the street corner while Mr. Dursley looks at them with confusion. Each person has a different colorful outfit, including one man in a bright emerald-green cloak. The scene is bustling, filled with laughter and excitement, with trees and shops in the background. Cartoonish style, with color.', "Inside Mr. Dursley's office, he sits with his back to the window, oblivious to the owls flying by outside. The room is filled with papers and tools, depicting his serious demeanor. Mr. Dursley has furrowed eyebrows, and his office is cluttered with drill equipment. The window shows a blurry owl in the daylight. Cartoonish style, with color. ", 'At lunchtime, Mr. Dursley walks past cloaked figures outside a bakery, gripping a bag of donuts. He squints his eyes at the peculiar gathering that seems to be celebrating. The bakery has a bright sign, and there are doughnuts displayed in the window, adding color to the scene. Cartoonish style, with color.', 'Back at home, Mr. Dursley is frozen in his armchair while watching the news about owls and shooting stars. The TV shows images of owls flying around, while worms and stars float around him symbolically representing his worry. His expression is shocked, and the room is cozy but tense. Cartoonish style, with color.', "Mr. Dursley nervously asks his wife about her sister and hears news about strange happenings, while Mrs. Dursley looks angry and surprised. She's wearing a floral dress and is holding a cup of tea with a tense expression. The kitchen is warm, illuminated by the afternoon sun streaming in. Cartoonish style, with color.", 'Dumbledore, portrayed as a tall, old man with long silver hair and a bright blue robe, appears at night on Privet Drive with a twinkle in his eye. He rummages through his cloak near a street lamp, and a gentle cat watches him curiously. The street is dark, with only a few stars shining above, setting a mysterious mood. Cartoonish style, with color.', 'Professor McGonagall is seen transforming from a tabby cat into a woman in a green cloak, looking stern but kind. Her hair is in a tight bun, and she wears square glasses. She stands beside Dumbledore, looking both curious and irritated in the dim light of dusk. Cartoonish style, with color.', 'Dumbledore and Professor McGonagall discuss the Potters while on a brick wall, lost in serious conversation. Dumbledore has a friendly smile, while McGonagall appears anxious and ruffled. Soft lights illuminate their faces, while shadows create an air of mystery around them. Cartoonish style, with color.', 'A giant motorcycle soars through the sky, landing with a thud in front of Dumbledore and McGonagall. Hagrid, a gigantic man with tangled hair and a wild beard, steps off while holding a bundle of blankets. The motorcycle looks impressive with shiny chrome and colorful details, contrasting the night sky. Cartoonish style, with color.', 'As Dumbledore carefully holds baby Harry in his arms, the baby has a little tuft of jet-black hair and a lightning bolt-shaped scar on his forehead. Hagrid watches with teary eyes, and the moonlight highlights the innocence of baby Harry. The background is a mixture of blues and purples, adding to the nighttime magic. Cartoonish style, with color.', 'Dumbledore sets baby Harry on the doorstep of the Dursleys’ house gently, tucking a letter into the blanket beside him. The steps are set against a cozy house background, with flowerpots and a warm light coming from inside. The atmosphere is heartfelt, with a hint of sadness as Hagrid looks on with a handkerchief. Cartoonish style, with color.', 'A beautiful cartoonish sky sparkles with stars as the Dursleys’ front door opens, revealing baby Harry sleeping peacefully. The scene conveys a sense of calm, with twinkling stars around baby Harry who is blissfully unaware of his importance. A warm light glows from the house, while a gentle breeze ruffles the bushes outside. Cartoonish style, with color.', 'As people toast to baby Harry across the country, you see joyful celebration with fireworks and happy friends holding glasses in relief and excitement. Everyone looks cheerful and colorful, with smiles all around as they talk cheerfully together, marking the special moment. Cartoonish style, with color.']
if __name__ == "__main__":
    outPutGeneration(input_prompts)
