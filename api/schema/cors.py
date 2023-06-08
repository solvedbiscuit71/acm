import os
import dotenv

dotenv.load_dotenv()
origins = os.getenv('ORIGINS').split(' ')
