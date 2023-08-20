from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO

# 初始化一個 Chrome 瀏覽器實例
driver = webdriver.Chrome()  # 請確保已經安裝了 Chrome 瀏覽器和相應的驅動程式

# 打開目標網頁
url = "https://24h.pchome.com.tw/prod/DBACNC-1900GK5VI?fq=/S/DBACCR"  # 請將這個 URL 替換為您想要訪問的網頁地址
driver.get(url)

# 等待頁面加載完成（您可能需要根據頁面的實際加載時間進行適當的等待）
driver.implicitly_wait(10)  # 在這裡等待 10 秒，您可以根據實際情況進行調整

# 找到要擷取的元素
target_element = driver.find_element(
    By.CLASS_NAME, "swiper-wrapper"
)  # 根據 class name 找到元素

# 獲取元素的位置和大小
element_location = target_element.location
element_size = target_element.size

# 擷取元素的截圖
screenshot = driver.get_screenshot_as_png()
cropped_image = Image.open(BytesIO(screenshot)).crop(
    (
        element_location["x"],
        element_location["y"],
        element_location["x"] + element_size["width"],
        element_location["y"] + element_size["height"],
    )
)

# 儲存截圖
cropped_image.save("cropped_image.png")  # 請將檔案名稱替換為您想要儲存的檔案名稱

# 關閉瀏覽器
driver.quit()
