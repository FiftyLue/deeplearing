from migrations.load_data import *
import matplotlib.pyplot as plt


# 测试检查点
from migrations.model import inference


def eval(filepath):
    N_CLASSES = 2
    IMG_SIZE = 208
    BATCH_SIZE = 1
    CAPACITY = 200

    logs_dir = 'model'     # 检查点目录

    sess = tf.Session()
    train_list = get_files(filepath)
    image_train_batch, label_train_batch = get_batch(train_list, IMG_SIZE, BATCH_SIZE, CAPACITY, True)
    train_logits = inference(image_train_batch, N_CLASSES)
    train_logits = tf.nn.softmax(train_logits)  # 用softmax转化为百分比数值

    # 载入检查点
    saver = tf.train.Saver()
    print('\n载入检查点...')
    print(logs_dir)
    model_checkpoint_path = 'C:\\Users\\Administrator\\PycharmProjects\\djangotest\\cmdb\\migrations\\model\model.ckpt-9999'

    if model_checkpoint_path:
        global_step = model_checkpoint_path.split('/')[-1].split('-')[-1]
        print(global_step)
        saver.restore(sess, model_checkpoint_path)
        print('载入成功，global_step = %s\n' % global_step)
    else:
        print('没有找到检查点')
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    try:
            image, prediction = sess.run([image_train_batch, train_logits])
            max_index = np.argmax(prediction)
            if max_index == 0:
                label = '%.2f%% 的概率是猫' % (prediction[0][0] * 100)
            else:
                label = '%.2f%% 的概率是狗' % (prediction[0][1] * 100)

            plt.imshow(image[0])
            plt.title(label)
            plt.show()


    except tf.errors.OutOfRangeError:
        print('Done.')
    finally:
        coord.request_stop()

    coord.join(threads=threads)
    sess.close()
    return label
if __name__ == '__main__':
    eval('C:\\Users\\Administrator\\Desktop\\data\\test\\5.jpg')