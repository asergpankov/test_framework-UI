import pytest

from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgetsPage:
    class TestAccordianPage:
        def test_accordian_structure(self, driver):
            accordian = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian.open_browser()
            first_title, first_content = accordian.check_accordian_structure('first')
            second_title, second_content = accordian.check_accordian_structure('second')
            third_title, third_content = accordian.check_accordian_structure('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 11
            assert second_title == 'Where does it come from?' and second_content > 11
            assert third_title == 'Why do we use it?' and third_content > 222

    class TestAutoCompletePage:
        def test_auto_complete_multi(self, driver):
            auto_complete = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete.open_browser()
            colors_from_gen = auto_complete.fill_colors_multiply_input()
            colors_res = auto_complete.check_colors_multiply_input()
            assert colors_from_gen == colors_res, 'diffs in list of colors'

        def test_remove_all_colors_from_multi_with_x_sign(self, driver):
            auto_complete = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete.open_browser()
            auto_complete.fill_colors_multiply_input()
            nums_before, nums_after = auto_complete.remove_color_from_multiply_with_x()
            assert nums_before > nums_after, 'color was not removed as expected'

        def test_remove_colors_from_multi_with_backspace(self, driver):
            auto_complete = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete.open_browser()
            auto_complete.fill_colors_multiply_input()
            clrs_before_remove, clrs_after_remove = auto_complete.remove_color_from_multiply_with_backspace()
            assert clrs_before_remove > 0
            assert clrs_after_remove == 1

        def test_remove_colors_from_multi_with_main_x(self, driver):
            auto_complete = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete.open_browser()
            auto_complete.fill_colors_multiply_input()
            clrs_before_remove, clrs_after_remove = auto_complete.remove_all_colors_from_multi_with_main_x()
            assert clrs_before_remove > 0
            assert clrs_after_remove == 0

        def test_auto_complete_single(self, driver):
            auto_complete = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete.open_browser()
            color_from_gen = auto_complete.fill_color_single_input()
            colors_res = auto_complete.check_color_single_input()
            assert color_from_gen == colors_res, 'colors are not equal'
            # bugs: - color could not be deleted, - "voilet" is not correct color