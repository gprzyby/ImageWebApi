from unittest import mock
from django.test import TestCase
from PIL import Image
from manipulationapi.services import crop_image, scale_image

from rest_framework.exceptions import ValidationError


class TestImageService(TestCase):
    def setUp(self) -> None:
        self.mock_image = Image.new("RGB", (200, 200), (100, 100, 100))

    def test_crop_image_validations(self):
        cases_to_test = (
            lambda: crop_image(self.mock_image, 0, 0, 1000, 1000),
            lambda: crop_image(self.mock_image, -1, -1, 10, 10),
            lambda: crop_image(self.mock_image, 0, 0, -19, 20),
            lambda: crop_image(self.mock_image, 10, 10, 0, 0),
        )

        for test_case in cases_to_test:
            self.assertRaises(ValidationError, test_case)

    def test_crop_image_function_called(self):
        self.mock_image.crop = mock.MagicMock(name='crop_image')
        crop_image(self.mock_image, 0, 0, 10, 10)
        self.mock_image.crop.assert_called()
        self.mock_image.crop.assert_called_with(box=(0, 0, 10, 10))

    def test_scale_image_validation(self):
        test_cases = (
            lambda: scale_image(None, None),
            lambda: scale_image(self.mock_image, 0),
            lambda: scale_image(self.mock_image, None)
        )

        for test_case in test_cases:
            self.assertRaises(ValidationError, test_case)

    def test_scale_function_called(self):
        self.mock_image.resize = mock.MagicMock()
        scale_image(self.mock_image, 2.)
        self.mock_image.resize.assert_called()
        self.mock_image.resize.assert_called_with((400, 400))
