import pyclamd


def extensionAllowed(File_Name):
    extensions_indesirables = ['.exe', '.py', '.cpp', '.cxx', '.cc']
    return not any(File_Name.lower().endswith(ext) for ext in extensions_indesirables)


def contentAllowed(content):
    motifs_indesirables = ['system(', 'shell_exec(','cmd']
    return not any(motif in content for motif in motifs_indesirables)


def fileVerification(fileName):
    # Cr�er une instance du client ClamAV
    clamav = pyclamd.ClamdAgnostic()

    # V�rifier le fichier avec ClamAV
    resultat = clamav.scan_file(fileName)

    # V�rifier le r�sultat
    if resultat[fileName] == 'OK':
        print(f"The file {fileName} is clear.")
        return resultat[fileName]
    else:
        print(f"The file {fileName} have a malware : {resultat[fileName]}")
        return resultat[fileName]


