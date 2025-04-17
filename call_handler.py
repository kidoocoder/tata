from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream.quality import HighQualityAudio

# Initialize PyTgCalls with no client (will be assigned later in main.py)
pytgcalls = PyTgCalls(client=None)

# Function to join and play the audio in a voice chat
async def join_and_play(chat_id: int, audio_path: str):
    try:
        # Join the voice chat and play the audio
        await pytgcalls.join_group_call(
            chat_id,
            InputStream(
                audio_source=HighQualityAudio(audio_path)  # Using high-quality audio stream
            ),
            stream_type=None  # Type is None for basic audio stream
        )
    except Exception as e:
        print(f"Error in joining group call or playing audio: {e}")
