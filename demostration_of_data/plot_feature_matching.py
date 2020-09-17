# author: 龚潇颖(Xiaoying Gong)
# date： 2020/9/8 19:46  
# IDE：PyCharm 
# des: 此文件用于绘制两幅图，及其特征匹配的结果
# pts_1 和 pts_2 已经
# input(s)：
# output(s)：
import matplotlib.pyplot as plt
import numpy as np

# true为blue， false为black
match_colors = ['blue', 'black']
points_color = 'red'


def plot_image_pair_and_matching(img_1, img_2, pts_1, pts_2, match_result, is_gray=False):
    if is_gray:
        plt.imshow(np.hstack((img_1, img_2)), cmap='gray')
    else:
        plt.imshow(np.hstack((img_1, img_2)))

    plt.scatter(pts_1[:, 0], pts_1[:, 1], c=points_color)
    plt.scatter(pts_2[:, 0]+img_1.shape[1], pts_2[:, 1], c=points_color)

    true_matches_idx = np.argwhere(match_result == 1).flatten()
    false_matches_idx = np.argwhere(match_result == 0).flatten()

    for idx in false_matches_idx:
        plt.plot([pts_1[idx, 0], pts_2[idx, 0]+img_1.shape[1]], [pts_1[idx, 1], pts_2[idx, 1]], c=match_colors[1])

    for idx in true_matches_idx:
        plt.text((pts_1[idx, 0] + pts_2[idx, 0]+img_1.shape[1]) / 2, (pts_1[idx, 1] + pts_2[idx, 1]) / 2, idx)
        plt.plot([pts_1[idx, 0], pts_2[idx, 0]+img_1.shape[1]], [pts_1[idx, 1], pts_2[idx, 1]], c=match_colors[0])



if __name__ == '__main__':
    import scipy.io as io
    mat = io.loadmat("../dataset/mixture_dataset/5006.mat")
    ground_truth = mat["ground_truth"]
    print(ground_truth.flatten())
    print(np.sum(ground_truth) / len(ground_truth))
    plot_image_pair_and_matching(mat["img_x"], mat["img_y"], mat["X"], mat["Y"], mat["ground_truth"], is_gray=False)
    plt.show()
    # mat["X"] = np.delete(mat["X"], 3, axis=0).reshape([-1, 2])
    # mat["Y"] = np.delete(mat["Y"], 3, axis=0).reshape([-1, 2])
    # mat["ground_truth"] = np.delete(mat["ground_truth"], 3, axis=0).reshape([-1, 1])
    #
    # io.savemat('../dataset/chen_mixture_dataset/5004.mat', mat)
