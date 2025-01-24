import scipy.io

def read_mat_file(mat_file_name='TG119.mat'):
    mat_data = scipy.io.loadmat(mat_file_name)
    return mat_data

if __name__ == '__main__':
    mat_data = read_mat_file(mat_file_name='TG119.mat')
    print(mat_data.keys())

