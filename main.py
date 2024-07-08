"""
Este script é uma automação web que utiliza Selenium WebDriver com Chrome.
Ele navega até o Google, faz uma busca por "baixar python", clica no primeiro resultado da busca,
navega até o link de download desejado e clica no link final de download.

"""

from services.driver import ChromeDriver
from services.steps import DownloadPythonSteps


def run():
    try:
        """Inicializa o Driver"""
        chrome_driver = ChromeDriver()
        driver = chrome_driver.get_driver()

        # Obtém a classe com os passos para o download
        steps = DownloadPythonSteps(driver)

        # Abre o navegador para realizar a pesquisa
        browser_opened = steps.open_browser("https://www.google.com/")
        if browser_opened['error']:
            print(browser_opened['msg'])
            return None
        
        # Espera o campo de busca ser clicável e envia a busca
        searched = steps.search("baixar python")
        if searched['error']:
            print(searched['msg'])
            return None
        
        # Espera e clica no primeiro resultado da busca
        first_result_clicked = steps.click_first_result()
        if first_result_clicked['error']:
            print(first_result_clicked['msg'])
            return None

        # Espera e clica no link desejado na página seguinte
        download_link_clicked = steps.click_download_link()
        if download_link_clicked['error']:
            print(download_link_clicked['msg'])
            return None

        # Espera e clica no link final de download
        final_download_link_clicked = steps.click_final_download_link()
        if final_download_link_clicked['error']:
            print(final_download_link_clicked['msg'])
            return None

        # Espera o download ser concluído
        download_completed = steps.wait_for_download()
        if download_completed['error']:
            print(download_completed['msg'])
            return None

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == '__main__':
    run()
