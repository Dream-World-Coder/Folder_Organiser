
import os
import shutil
import time

# using a list would have been better
# TOTAL 84 FORMATS +- 1

class Org:
    general_folders = {
        'songs':['.mp3','.wav', '.ra'],
        'videos':['.mp4','.mov'],
        'images':['.jpg','.jpeg','.png','.webp','.gif','.tiff','.heif', '.avif'],
        'icons':['.svg','.ico'],
        'fonts':['.woff','.woff2'],
        'documents':['.pdf','.docx','.doc', '.pages','.cbz'],
        'spreadsheets':['.xls','.xlsx','.csv','.numbers','.key'],
        'text-files':['.txt', '.kl', '.d', '.ss', '.p', '.b', '.pu', '.abc', '.pp', '.sc', '.cm', '.po', '.command'],
        'jsons':['.json'],
        'codes':['.py','.s','.cs','.cp','.net', '.sh','.bat','.md','.exe','.cmd','.c','.i','.h','.cpp','.c++','.ipynb', '.html','.htm','.xml','.css','.js','.ts','.jsx','.scss','.java','.swift', '.php', '.mjs', '.pyi', '.mojo', '.f', '.f95', '.rust', '.go', '.ruby'],
        'sercet-keys':['.env'],
        'log-files':['.log'],
        'configs':['procfile'],
        'archives':['.zip', '.rar', '.tar', '.gz', '.7z']
    }
        
    def __init__(self) -> None:
        self.codes_folder = {
            'python':['.py','.pyi'],
            'jupyter-notebook':['.ipynb'],
            'mojo':['.mojo'],
            'c':['.c','.h', '.i'],
            'cpp':['.cpp','.cp', '.c++'],
            'html':['.html','.htm'],
            'xml':['.xml'],
            'css':['.css'],
            'sass':['.scss'],
            'javascript':['.js'],
            'typescript':['.ts'],
            'react':['.jsx'],
            'java':['.java'],
            'php':['.php'],
            'mjs':['.mjs'],
            'fortran':['.f', '.f95'],
            'rust':['.rust'],
            'go':['.go'],
            'ruby':['.ruby'],
            'swift':['.swift'],
            'shell-scripts':['.sh', '.bat', '.exe', '.cmd', '.s'],
            'md':['.md'],
            'c-sharp':['.cs','.net']
        }
        
        self.images_folder = {
            'jpg':['.jpg'],
            'jpeg':['.jpeg'],
            'png':['.png'],
            'web-photos':['.webp', '.avif'],
            'gifs':['.gif'],
            'tiffs':['.tiff'],
            'heifs':['.heif']
        }
        
        self.icons_folder = {
            'svgs':['.svg'],
            'favicons':['.ico']
        }
        
        self.videos_folder = {
            'mov':['.mov'],
            'mp4':['.mp4']
        }
        
        self.text_files_folder = {
            'txts':['.txt'],
            'others':[self.general_folders['text-files'][1:]]
        }
        
        self.documents_folder = {
            'pdf':['.pdf'],
            'cbz':['.cbz'],
            'pages':['.pages'],
            'word':['.doc', '.docx']
        }
        
        self.spreadsheets_folder = {
            'excel':['.xls', '.xlsx'],
            'numbers':['.numbers'],
            'csv':['.csv']
        }

    # <>-::---:---::-<>  <>-::---:---::-<>  <>-::---:---::-<>   <>-::---:---::-<>#

    def makeAlternateFilePath(self, path:str) -> str:
        i = 1
        fname, ext = os.path.splitext(path)
        newPath = f'{fname}_{i}{ext}'
        while os.path.exists(newPath):
            newPath = f'{fname}_{i}{ext}'
            i += 1
        return newPath
            
    # <>-::---:---::-<>  <>-::---:---::-<>  <>-::---:---::-<>   <>-::---:---::-<>#
    # why self is defined inside methods only?
    # print(self.codes_folder['python'])
    # folders = self.general_folders will give error
    def organise(self, folders=general_folders, rename=True, delete=False, tree=True, exceptions=[]):
        """ 
            *** MODES:
                **  <rename> the new filename will be changed 
                    and the existing file name will be the same

                **  <delete> the existing file will be deleted
                    and the new file will be moved to the folder

                **  <rename> and <delete> both cannot be applied
                    at once
                
                **  if both <rename> and <delete> are applied
                    then if the destination file path already exists
                    then the file will be skipped.
                    
            *** <tree> - if True, then organises subdirectories also
                    
            ***  <exceptions> - list of files that will be ignored
            
            ***  <.{ext}> and <filename.> will be ignored
        """
        try:
            assets_in_cwd = os.listdir()
            for asset in assets_in_cwd:
                if os.path.isfile(asset):
                    file = asset
                    if file == os.path.basename(__file__) or file in exceptions:
                        print(f'{file} is skipped.')
                        continue
                    
                    fExt = os.path.splitext(file)[1]
                    
                    for k in list(folders.keys()):
                        for v in folders[k]:
                            if  v == fExt:
                                dir = k
                                if not os.path.exists(dir):
                                    os.mkdir(dir)
                                elif os.path.exists(dir) and os.path.isfile(dir):
                                    os.remove(dir)
                                    os.mkdir(dir)
                                else:
                                    None

                                if not rename and not delete:
                                    try:
                                        shutil.move(src=file, dst=dir)
                                        print(f'{file} moved to {dir}.\n')
                                    except shutil.Error as e:
                                        print(f'Error moving {file}: {e}\nSkipping it.')
                                
                                elif rename and not delete:
                                    try:
                                        shutil.move(src=file, dst=dir)
                                        print(f'{file} moved to {dir}.\n')
                                    except shutil.Error as e:
                                        destination_path = f'{dir}/{file}'
                                        print(f'{destination_path=} Already exists.')
                                        if os.path.exists(destination_path):
                                            path2 = self.makeAlternateFilePath(destination_path)
                                            new_name = os.path.basename(path2)
                                            os.rename(file, new_name)
                                            print(f'{file} renamed to {new_name}.')
                                            shutil.move(src=new_name, dst=dir)
                                            print(f'{new_name} moved to {dir}.\n')
                                            
                                elif not rename and delete:
                                    try:
                                        shutil.move(src=file, dst=dir)
                                        print(f'{file} moved to {dir}.\n')
                                    except shutil.Error as e:
                                        print(f'Error moving {file}: {e}\n Deleting it.')
                                        path = f'{dir}/{file}'
                                        os.remove(path)
                                        print(f'{path} deleted.')
                                        shutil.move(src=file, dst=dir)
                                        print(f'{file} moved to {dir}.\n')
                                
                                else:
                                    string = f'''
                                        only possible options are:
                                            rename | delete
                                                true  |  false
                                                false |  false
                                                false |  true
                                        '''
                                    print(string)

            if tree:
                current_dirs = [dir for dir in os.listdir() if os.path.isdir(dir)]
                to_organise_further = ['codes', 'images', 'icons', 'videos', 'text-files' , 'documents', 'spreadsheets']
                for dir in current_dirs:
                    if dir in to_organise_further:
                        os.chdir(dir)
                        if dir == 'codes':
                            self.organise(folders=self.codes_folder, exceptions=[''], tree=False)
                        elif dir == 'images':
                            self.organise(folders=self.images_folder, exceptions=[''], tree=False)
                        elif dir == 'icons':
                            self.organise(folders=self.icons_folder, exceptions=[''], tree=False)
                        elif dir == 'videos':
                            self.organise(folders=self.videos_folder, exceptions=[''], tree=False)
                        elif dir == 'text-files':
                            self.organise(folders=self.text_files_folder, exceptions=[''], tree=False)
                        elif dir == 'documents':
                            self.organise(folders=self.documents_folder, exceptions=[''], tree=False)
                        elif dir == 'spreadsheets':
                            self.organise(folders=self.spreadsheets_folder, exceptions=[''], tree=False)
                        os.chdir('..')
                        
        except Exception as e:
            print(e)
            
        finally:
            print('done, *_* >> •_• >> ^_^ \n\n')
                
    # <>-::---:---::-<>  <>-::---:---::-<>  <>-::---:---::-<>   <>-::---:---::-<>#
        
    def organise_for_flask(self):
        ...
    
    # <>-::---:---::-<>  <>-::---:---::-<>  <>-::---:---::-<>   <>-::---:---::-<>#


def main():
    obj = Org()
    obj.organise(rename=True, delete=False, exceptions=['m.py'])
    # obj.organise_for_flask(exceptions=['m.py'])
    
    
if __name__ == "__main__":
    main()
