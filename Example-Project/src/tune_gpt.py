
import os
import requests
import gpt_2_simple as gpt2

def get_model_name(model_size):
    if 'large' in model_size:
        model_name = '774M'

    elif 'medium' in model_size: 
        model_name = "355M"

    elif 'small' in model_size:
        model_name = "124M"
    
    return model_name

def get_file_name(bucket, path, file_name):
    
    # for the exceedingly time-constrained    
    os.system('aws s3 cp s3://{}/{}/{} .'.format(bucket, path, file_name))
    
    return file_name

def save_to_s3(txt, bucket, path, out_file):
    
    # say hello to cloudwatch
    print (txt)

    with open(outfile, 'w') as f:
        f.write(txt)        

    # could also save the trained model to s3 here
#     os.environ.get('SM_MODEL_DIR')
        
    os.system('aws s3 cp {} s3://{}/{}/output/'.format(outfile, bucket, path))

if __name__ == "__main__":
            
    bucket = bucket
    
    path = path
        
    model_name = get_model_name('large')

    if not os.path.isdir(os.path.join("models", model_name)):
        print(f"Downloading {model_name} model...")
        gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/model_name/

    file_name = get_file_name(bucket, path, 'sagemaker-examples.txt')

    sess = gpt2.start_tf_sess()

    print ('fine tuning on {}'.format(file_name))
    
    gpt2.finetune(sess,
                  file_name,
                  model_name=model_name,
                  steps=1000)   # steps is max number of training steps

    txt = gpt2.generate(sess, return_as_list = True)[0]
    
    save_to_s3(txt, bucket, path, 'output.txt')
