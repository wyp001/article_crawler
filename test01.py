from article_crawler.csdn.csdn_crawler import CSDNCrawler
from article_crawler.jianshu.jianshu_crawler import JianshuCrawler
from article_crawler.juejin.juejin_crawler import JuejinCrawler

## 测试代码
if __name__ == '__main__':

    output_folder = "D:\\Test\\01TestData\\"

    # 简书
    # url = "https://www.jianshu.com/p/f864bbd93691"
    # crawler = JianshuCrawler(url=url, output_folder=output_folder)

    # # csdn
    # url = "https://blog.csdn.net/qq_32419139/article/details/131187884"
    # crawler = CSDNCrawler(url=url, output_folder=output_folder)

    # 掘金
    url = "https://juejin.cn/post/7372765277459136522"
    crawler = JuejinCrawler(url=url, output_folder=output_folder)

    crawler.start()