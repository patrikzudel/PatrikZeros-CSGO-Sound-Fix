import json
import subprocess

# Function to get all different sinks that is tied to CSGO
def getSinkIndex(inputs):
    indices = []
    found_index = False
    found_csgo = False

    # Split the input string into lines
    lines = inputs.split('\n')
    # Loop through the lines
    for line in lines:
        if "index:" in line:
            # If we have already found the csgo line, add the previous index to the list of indices
            if found_csgo:
                indices.append(index)
            # Extract the index value from the line
            index = line.split(':')[1].strip()
            # Set the found_index flag to True
            found_index = True
            # Reset the found_csgo flag
            found_csgo = False
        elif found_index and "csgo_linux64" in line:
            # If we have already found an index and we have found the csgo line, set the found_csgo flag to True
            found_csgo = True
    # Add the last index value to the list of indices if we found the csgo line before reaching the end of the input
    if found_csgo:
        indices.append(index)
    return indices

settingsFile = open("settings.txt", "r")
settings = json.loads(settingsFile.read().replace('\n', ''))
settingsFile.close()
result = subprocess.run(["pacmd", "list-sink-inputs"], stdout=subprocess.PIPE)
output = result.stdout.decode("utf-8")
indexes = getSinkIndex(output)



def changeVolume(vol : float, index : str):
    subprocess.run(["pacmd", "set-sink-input-volume", index, str(int(
        vol*65536))])
    

def deathVolume():
    for index in indexes:
        changeVolume(float(settings['deathVolume']), index)


def bombVolume():
    for index in indexes:
        changeVolume(float(settings['bombExplosionVolume']), index)


def flashVolume():
    for index in indexes:
        changeVolume(float(settings['flashVolume']), index)


def highVolume():
    for index in indexes:
        changeVolume(float(1), index)


if __name__ == "__main__":
    pass