
def pic_circle():
    # initialize our canvas as a 300x300 pixel image with 1 channel
    canvas3 = np.zeros((300, 300, 1), dtype="uint8")
    cv2.circle(canvas3, (30,50), 50, 1, -1)
    plt.subplot(221), plt.imshow(canvas3, cmap='gray')
    plt.title('Single Region'), plt.xticks([]), plt.yticks([])
    return canvas3
