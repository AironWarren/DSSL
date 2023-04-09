import allure

from models.price_list import PriceListPage
from models.video_recorders import VideoRecorders
from models.working_with_files import WorkingWithFiles, resources_dir


@allure.tag('web')
@allure.label('owner', 'AironWarren')
@allure.link('https://www.dssl.ru/', name='Testing')
def test_DSSL_company_online_store(open_browser):
    price_list_page = PriceListPage()
    video_recorders = VideoRecorders()
    working_with_files = WorkingWithFiles()

    price_list_page.submit_price_list()

    price_list_page.download_price_list()

    video_recorders.go_to_the_subsection()

    video_recorders.submit_filter()

    video_recorders.enter_the_price('100000', '350000')

    video_recorders.choose_a_brand()

    video_recorders.show_options_for_the_selected_parameters()

    row = working_with_files.number_of_lines_in_the_file(resources_dir + '\DSSL_price.xlsx')

    working_with_files.del_file(resources_dir + '\DSSL_price.xlsx')



