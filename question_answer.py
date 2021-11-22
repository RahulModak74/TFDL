from ktrain import text
import os
import shutil
text.SimpleQA.initialize_index('index')
text.SimpleQA.index_from_folder(folder_path='entertainment',index_dir='index')
qa = text.SimpleQA('index')
answers = qa.ask('who who had a global hit with where is the love?')
print (qa.display_answers(answers[:5]))
