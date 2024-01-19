from botok import Text
import os
import argparse

def botok_tokenize(input_path, output_dir):
    
    if os.path.isfile(input_path):
        
        with open(input_path, 'r') as f:
            output_path = os.path.join(output_dir, os.path.basename(input_path)[:-4] + '_tokenized.txt')
            
            try:
                with open(output_path, 'w') as g:
                    g.write(Text(f.read()).tokenize_words_raw_text)
                    
            except:
                os.mkdir(output_dir)
                with open(output_path, 'w') as g:
                    g.write(Text(f.read()).tokenize_words_raw_text)
                    
                    
    elif os.path.isdir(input_path):
        
        for file in os.listdir(input_path):
            with open(os.path.join(input_path, file)) as f:
                output_path = os.path.join(output_dir, 'tokenized_' + file)
                
                try:
                    with open(output_path, 'w') as g:
                        g.write(Text(f.read()).tokenize_words_raw_text)
                        
                except:
                    os.mkdir(output_dir)
                    with open(output_path, 'w') as g:
                        g.write(Text(f.read()).tokenize_words_raw_text)
                    
def main():
    parser = argparse.ArgumentParser(description='Tokenize a file or directory using botok')
    parser.add_argument('path', help='Path to a file or a directory')
    args = parser.parse_args()
    botok_tokenize(args.path)

if __name__ == '__main__':
    main()
                    