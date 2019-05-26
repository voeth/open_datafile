class Fileopener():
    def unfold(self,file_path=''):
        import pandas as pd
        from glob import glob
        
        if glob(str(file_path))==[]:
            return 'Cannot find related file'
        else:
            frame = [pd.read_csv(file,sep='\t') for file in glob(str(file_path))]
            columns = [set(data.columns) for data in frame]
            for col in range(1,len(columns)):
                difference = columns[0].difference(columns[col])
                if difference !={}:
                    break
            if not difference:
                # It is better to integrate the data frames of each file and integrate them when all the file column labels are the same.
                all_frame = pd.concat(frame) 
                return pd.DataFrame(all_frame),file_path
            else:
                return frame,file_path
            
    def DataSize(self,file_path=''):
        import pandas as pd 
        from glob import glob

        if glob(str(file_path))==[]:
            return 'Cannot find related file'
        else:
            frame = [pd.read_csv(file,sep='\t') for file in glob(str(file_path))]
            dataFrame = []
            for count in range(len(frame)):
                dataFrame.append([glob(str(file_path))[count],len(frame[count]),len(frame[count].columns),list(frame[count].columns)])
            return pd.DataFrame(dataFrame,columns=['file_name','row','col','columns_name'])