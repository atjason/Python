
import os


def search_folder(folder, ext):
  results = []

  for item in os.listdir(folder):
    file_path = os.path.join(folder, item)
    
    if os.path.isfile(file_path):
      if file_path.endswith(ext):
        results.append(file_path)

    elif os.path.isdir(file_path):
      results += search_folder(file_path, ext)

  return results


print search_folder(".", ".py")

