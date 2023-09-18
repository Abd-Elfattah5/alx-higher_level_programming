#!/usr/bin/python3
"""Defines unittests for base.py
"""
import sys
import unittest
import pycodestyle
import json
import models
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """unit test class for testing the base class's functions"""

    def setUp(self):
        """initializing necessary values"""
        self.r1 = Rectangle(1, 2, 3, 4)
        self.r2 = Rectangle(5, 6, 7, 8, 11)
        self.r3 = Rectangle(12, 14)

        self.s1 = Square(15, 16, 17)
        self.s2 = Square(18, 19, 20, 104)
        self.s3 = Square(21)

    def test_shebang(self):
        """checking shebang sign"""
        with open("models/base.py", "r") as my_file:
            line = my_file.readline()
            self.assertEqual(line, '#!/usr/bin/python3\n')

    def test_conformance(self):
        """pycodestyle is followed"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_func_presence(self):
        """all the functions are present"""
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "save_to_file_csv"))
        self.assertTrue(hasattr(Base, "load_from_file_csv"))
        self.assertTrue(hasattr(Base, "draw"))

    def test_documentation(self):
        """every function has a documentation"""
        self.assertIsNotNone(models.base.__doc__)
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.save_to_file_csv.__doc__)
        self.assertIsNotNone(Base.load_from_file_csv.__doc__)
        self.assertIsNotNone(Base.draw.__doc__)

    def test_init(self):
        """checking Base __init__ function"""
        b = Base()  # regular id
        self.assertEqual(b.id, Base._Base__nb_objects)

        b_none = Base(None)  # regular id after b
        b_max_p = Base(sys.maxsize)  # should have the highest positive int
        b_0 = Base(0)  # zero id
        b_after = Base()  # should have the next id of b_none
        b_n = Base(-1)  # negative number
        b_max_neg = Base(-sys.maxsize)  # should have the highest negative int
        b_list = Base([1, 2, 3])  # should have id as a list
        b_dict = Base({"a": 1, "b": 2, "c": 3})  # should have id as a dict
        b_float = Base(2.5)  # float id
        b_max_f = Base(float('inf'))  # should have the maximum float num as id
        b_max_f_n = Base(-float('inf'))  # id the maximum negative float

        self.assertEqual(b.id, b_none.id - 1)
        self.assertEqual(b_max_p.id, sys.maxsize)
        self.assertEqual(b_0.id, 0)
        self.assertEqual(b_after.id, b_none.id + 1)
        self.assertEqual(b_n.id, -1)
        self.assertEqual(b_max_neg.id, -sys.maxsize)
        self.assertEqual(b_list.id, [1, 2, 3])
        self.assertEqual(b_dict.id, {"a": 1, "b": 2, "c": 3})
        self.assertEqual(b_float.id, 2.5)
        self.assertEqual(b_max_f.id, float('inf'))
        self.assertEqual(b_max_f_n.id, -float('inf'))

    def test_to_json_stirng(self):
        """checking to_json_string function"""

        lst1 = [self.r1.to_dictionary(),
                self.r2.to_dictionary(),
                self.r3.to_dictionary()]

        lst2 = [self.s1.to_dictionary(),
                self.s2.to_dictionary(),
                self.s3.to_dictionary()]

        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        with self.assertRaises(TypeError):
            Base.to_json_string()

        self.assertEqual(Base.to_json_string(lst1), json.dumps(lst1))
        self.assertEqual(Base.to_json_string(lst1[:2]), json.dumps(lst1[:2]))
        self.assertEqual(Base.to_json_string(lst1[:1]), json.dumps(lst1[:1]))

        self.assertEqual(Base.to_json_string(lst2), json.dumps(lst2))
        self.assertEqual(Base.to_json_string(lst2[:2]), json.dumps(lst2[:2]))
        self.assertEqual(Base.to_json_string(lst2[:1]), json.dumps(lst2[:1]))

        self.assertIsInstance(Base.to_json_string(lst1), str)
        self.assertIsInstance(Base.to_json_string(lst2), str)

    def test_from_json_string(self):
        """checking from_json_string"""

        lst_dict_rct = [self.r1.to_dictionary(),
                        self.r2.to_dictionary(),
                        self.r3.to_dictionary()]

        lst_dict_sqr = [self.s1.to_dictionary(),
                        self.s2.to_dictionary(),
                        self.s3.to_dictionary()]

        lst_dict_mix = [self.r1.to_dictionary(),
                        self.s2.to_dictionary(),
                        self.r3.to_dictionary(),
                        self.s3.to_dictionary()]

        string_json_rct = Base.to_json_string(lst_dict_rct)
        string_json_sqr = Base.to_json_string(lst_dict_sqr)
        string_json_mix = Base.to_json_string(lst_dict_mix)

        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])
        with self.assertRaises(TypeError):
            Base.from_json_string()

        self.assertEqual(Base.from_json_string(string_json_rct), lst_dict_rct)
        self.assertEqual(Base.from_json_string(string_json_sqr), lst_dict_sqr)
        self.assertEqual(Base.from_json_string(string_json_mix), lst_dict_mix)

        self.assertEqual(type(Base.from_json_string(string_json_rct)), list)
        self.assertEqual(type(Base.from_json_string(string_json_sqr)), list)

    def test_save_to_file(self):
        """checking saving to normal file"""
        Rectangle.save_to_file([self.r1])
        with open("Rectangle.json", "r") as my_file:
            lines = my_file.read()
            string = Base.to_json_string([self.r1.to_dictionary()])
            self.assertEqual(lines, string)

        Rectangle.save_to_file([self.r1, self.r2, self.r3])
        with open("Rectangle.json", "r") as my_file:
            lines = my_file.read()
            string = Base.to_json_string([self.r1.to_dictionary(),
                                          self.r2.to_dictionary(),
                                          self.r3.to_dictionary()])

            self.assertEqual(lines, string)

        Square.save_to_file([self.s1])
        with open("Square.json", "r") as my_file:
            lines = my_file.read()
            string = Base.to_json_string([self.s1.to_dictionary()])
            self.assertEqual(lines, string)

        Square.save_to_file([self.s1, self.s2, self.s3])
        with open("Square.json", "r") as my_file:
            lines = my_file.read()
            string = Base.to_json_string([self.s1.to_dictionary(),
                                          self.s2.to_dictionary(),
                                          self.s3.to_dictionary()])

            self.assertEqual(lines, string)

        Rectangle.save_to_file(None)
        with open("Rectangle.json") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "[]")

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        Square.save_to_file(None)
        with open("Square.json") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "[]")

        Square.save_to_file([])
        with open("Square.json") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "[]")

        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_load_from_file(self):
        """checking on loading from fils"""
        lst_rec = [self.r1, self.r2, self.r3]
        lst_sqr = [self.s1, self.s2, self.s3]

        output_list_rec = Rectangle.load_from_file()
        output_list_sqr = Square.load_from_file()

        self.assertEqual(output_list_rec, [])
        self.assertEqual(output_list_sqr, [])
        self.assertEqual(type(output_list_rec), list)
        self.assertEqual(type(output_list_sqr), list)
        self.assertEqual(len(output_list_rec), 0)
        self.assertEqual(len(output_list_sqr), 0)

        Rectangle.save_to_file(None)
        Square.save_to_file(None)

        output_list_rec = Rectangle.load_from_file()
        output_list_sqr = Square.load_from_file()

        self.assertEqual(output_list_rec, [])
        self.assertEqual(output_list_sqr, [])
        self.assertEqual(type(output_list_rec), list)
        self.assertEqual(type(output_list_sqr), list)
        self.assertEqual(len(output_list_rec), 0)
        self.assertEqual(len(output_list_sqr), 0)

        Rectangle.save_to_file(lst_rec)
        Square.save_to_file(lst_sqr)

        output_list_rec = Rectangle.load_from_file()
        output_list_sqr = Square.load_from_file()

        self.assertEqual(type(output_list_rec), list)
        self.assertEqual(type(output_list_sqr), list)
        self.assertEqual(len(output_list_rec), 3)
        self.assertEqual(len(output_list_sqr), 3)

        for rec in output_list_rec:
            self.assertIsInstance(rec, Rectangle)

        for sqr in output_list_sqr:
            self.assertIsInstance(sqr, Square)

        self.assertEqual(str(self.r1), str(output_list_rec[0]))
        self.assertEqual(str(self.r2), str(output_list_rec[1]))
        self.assertEqual(str(self.r3), str(output_list_rec[2]))

        self.assertIsNot(self.r1, output_list_rec[0])
        self.assertIsNot(self.s1, output_list_sqr[0])

        self.assertEqual(self.r1.width, output_list_rec[0].width)
        self.assertEqual(self.r1.height, output_list_rec[0].height)
        self.assertEqual(self.r1.x, output_list_rec[0].x)
        self.assertEqual(self.r1.y, output_list_rec[0].y)
        self.assertEqual(self.r1.id, output_list_rec[0].id)

        self.assertEqual(self.s1.size, output_list_sqr[0].size)
        self.assertEqual(self.s1.x, output_list_sqr[0].x)
        self.assertEqual(self.s1.y, output_list_sqr[0].y)
        self.assertEqual(self.s1.id, output_list_sqr[0].id)

        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_creat(self):
        """checking create function"""
        lst_dict_rec = [self.r1.to_dictionary(),
                        self.r2.to_dictionary(),
                        self.r3.to_dictionary()]

        lst_dict_sqr = [self.s1.to_dictionary(),
                        self.s2.to_dictionary(),
                        self.s3.to_dictionary()]

        r_test = [Rectangle.create(**d) for d in lst_dict_rec]
        s_test = [Square.create(**d) for d in lst_dict_sqr]

        for i in range(3):
            self.assertEqual(r_test[i].to_dictionary(), lst_dict_rec[i])

        for i in range(3):
            self.assertEqual(s_test[i].to_dictionary(), lst_dict_sqr[i])

        self.assertEqual(str(r_test[1]), "[Rectangle] (11) 7/8 - 5/6")
        self.assertEqual(str(s_test[1]), "[Square] (104) 19/20 - 18")

        self.assertIsNot(r_test[0], self.r1)
        self.assertIsNot(r_test[1], self.r2)
        self.assertIsNot(r_test[2], self.r3)

        self.assertIsNot(s_test[0], self.s1)
        self.assertIsNot(s_test[1], self.s2)
        self.assertIsNot(s_test[2], self.s3)

    def test_save_to_csv(self):
        """testing saving to csv file"""
        Rectangle.save_to_file_csv([self.r2])
        with open("Rectangle.csv", "r") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "11,5,6,7,8\n")

        Rectangle.save_to_file_csv([self.r1, self.r2, self.r3])
        with open("Rectangle.csv", "r") as my_file:
            lines = my_file.read()
            temp = "{},1,2,3,4\n11,5,6,7,8\n{},12,14,0,0\n"
            self.assertEqual(lines,
                             temp.format(self.r1.id,
                                         self.r3.id))

        Square.save_to_file_csv([self.s2])
        with open("Square.csv", "r") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "104,18,19,20\n")

        Square.save_to_file_csv([self.s1, self.s2, self.s3])
        with open("Square.csv", "r") as my_file:
            lines = my_file.read()
            temp = "{},15,16,17\n104,18,19,20\n{},21,0,0\n"
            self.assertEqual(lines, temp.format(self.s1.id,
                                                self.s3.id))

        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "[]")

        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "[]")

        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

        Square.save_to_file_csv(None)
        with open("Square.csv") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "[]")

        Square.save_to_file_csv([])
        with open("Square.csv") as my_file:
            lines = my_file.read()
            self.assertEqual(lines, "[]")

        with self.assertRaises(TypeError):
            Square.save_to_file_csv()

    def test_load_from_csv(self):
        """checking load from csv file"""

        lst_rec = [self.r1, self.r2, self.r3]
        lst_sqr = [self.s1, self.s2, self.s3]

        output_list_rec = Rectangle.load_from_file_csv()
        output_list_sqr = Square.load_from_file_csv()

        self.assertEqual(output_list_rec, [])
        self.assertEqual(output_list_sqr, [])
        self.assertEqual(type(output_list_rec), list)
        self.assertEqual(type(output_list_sqr), list)
        self.assertEqual(len(output_list_rec), 0)
        self.assertEqual(len(output_list_sqr), 0)

        Rectangle.save_to_file_csv(None)
        Square.save_to_file_csv(None)

        output_list_rec = Rectangle.load_from_file_csv()
        output_list_sqr = Square.load_from_file_csv()

        self.assertEqual(output_list_rec, [])
        self.assertEqual(output_list_sqr, [])
        self.assertEqual(type(output_list_rec), list)
        self.assertEqual(type(output_list_sqr), list)
        self.assertEqual(len(output_list_rec), 0)
        self.assertEqual(len(output_list_sqr), 0)

        Rectangle.save_to_file_csv(lst_rec)
        Square.save_to_file_csv(lst_sqr)

        output_list_rec = Rectangle.load_from_file_csv()
        output_list_sqr = Square.load_from_file_csv()

        self.assertEqual(type(output_list_rec), list)
        self.assertEqual(type(output_list_sqr), list)
        self.assertEqual(len(output_list_rec), 3)
        self.assertEqual(len(output_list_sqr), 3)

        for rec in output_list_rec:
            self.assertIsInstance(rec, Rectangle)

        for sqr in output_list_sqr:
            self.assertIsInstance(sqr, Square)

        self.assertEqual(str(self.r1), str(output_list_rec[0]))
        self.assertEqual(str(self.r2), str(output_list_rec[1]))
        self.assertEqual(str(self.r3), str(output_list_rec[2]))

        self.assertIsNot(self.r1, output_list_rec[0])
        self.assertIsNot(self.s1, output_list_sqr[0])

        self.assertEqual(self.r1.width, output_list_rec[0].width)
        self.assertEqual(self.r1.height, output_list_rec[0].height)
        self.assertEqual(self.r1.x, output_list_rec[0].x)
        self.assertEqual(self.r1.y, output_list_rec[0].y)
        self.assertEqual(self.r1.id, output_list_rec[0].id)

        self.assertEqual(self.s1.size, output_list_sqr[0].size)
        self.assertEqual(self.s1.x, output_list_sqr[0].x)
        self.assertEqual(self.s1.y, output_list_sqr[0].y)
        self.assertEqual(self.s1.id, output_list_sqr[0].id)

        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
