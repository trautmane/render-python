'''
default settings for render tests
'''
import os

DEFAULT_RENDER = {
    'host': 'http://renderhost',
    'port': 8080,
    'owner': 'renderowner',
    'project': 'renderproject',
    'client_scripts': '/path/to/client_scripts'
        }

DEFAULT_RENDER_CLIENT = dict(DEFAULT_RENDER, **{
    'client_script': '/path/to/client_scripts/run_ws_client.sh',
    'memGB': '2G'})

DEFAULT_RENDER_ENVIRONMENT_VARIABLES = {
    'RENDER_HOST': DEFAULT_RENDER['host'],
    'RENDER_PORT': DEFAULT_RENDER['port'],
    'RENDER_OWNER': DEFAULT_RENDER['owner'],
    'RENDER_PROJECT': DEFAULT_RENDER['project'],
    'RENDER_CLIENT_SCRIPTS': DEFAULT_RENDER['client_scripts']
        }

DEFAULT_RENDER_CLIENT_ENVIRONMENT_VARIABLES = dict(
    DEFAULT_RENDER_ENVIRONMENT_VARIABLES, **{
        'RENDER_CLIENT_SCRIPT': DEFAULT_RENDER_CLIENT['client_script'],
        'RENDER_CLIENT_HEAP': DEFAULT_RENDER_CLIENT['memGB']})

TEST_FILES_DIR = os.path.join(os.path.dirname(
    __file__), 'test_files')

TEST_TILESPECS_FILE = os.path.join(TEST_FILES_DIR, 'tilespecs.json')

TEST_THINPLATESPLINE_FILE = os.path.join(
        TEST_FILES_DIR,
        'thin_plate_spline.json')
TEST_THINPLATEROUGH_FILE = os.path.join(
        TEST_FILES_DIR,
        'thin_plate_from_rough.json')
TEST_THINPLATESPLINEAFFINE_FILE = os.path.join(
        TEST_FILES_DIR,
        'thin_plate_spline_affine.json')

INTERPOLATED_TRANSFORM_TILESPEC = os.path.join(
    TEST_FILES_DIR, 'tilespec_interpolated.json')

REFERENCE_TRANSFORM_TILESPEC = os.path.join(
    TEST_FILES_DIR, 'tilespec_ref.json')

REFERENCE_TRANSFORM_TILESPECS = os.path.join(
    TEST_FILES_DIR, 'tilespec_references.json')

REFERENCE_TRANSFORM_SPECS = os.path.join(
    TEST_FILES_DIR, 'transform_references.json')

NONLINEAR_TRANSFORM_KWARGS = {
    'className': "mpicbg.trakem2.transform.NonLinearCoordinateTransform",
    'dataString': (
        "5 21 1103.117269905359 -5.606757285805906 "
        "5.321142212984271 1041.3480932107918 -10.43426929509782 "
        "7.428382306562735 -14.137269334106124 7.299563138046944 "
        "-15.904206050362355 18.284978789358718 3.4106705605908587 "
        "-23.24346650864392 -22.18066749731861 -3.583245180840507 "
        "3.2706525226745384 27.117126387399466 20.96651792381158 "
        "-1.2219610254066424 -10.531856407305256 0.3306037423046746 "
        "2.054811912746283 28.849184526610635 34.799030853758985 "
        "-7.4227129043141495 -8.211918715339516 -27.434469512200955 "
        "-3.1066643785881 3.8503170392714026 1.7124046587349628 "
        "1.8506627747180158 4.886666182237065 -2.949889582798017 "
        "-4.5150121503501515 -11.363818954372583 -9.8507389567363 "
        "8.672520277073502 5.89027776049669 4.924363838689751 "
        "-1.4446630732848895 -2.3876262067533727 19.9189118558668 "
        "21.72003155506043 1991.9406329917294 2171.99091870329 "
        "5136325.014398676 4300827.048910938 5862798.046430213 "
        "1.4793145755295639E10 1.1081068898569233E10 1.1535665428036394E10 "
        "1.737179414476557E10 4.5383202598685734E13 3.1913868517100258E13 "
        "2.9612848039584566E13 3.403565936230745E13 5.43037094200083E13 "
        "1.45059294093077376E17 9.790266764463008E16 8.5058013431605168E16 "
        "8.7104768756103424E16 1.06057724033609104E17 1.75771529104524608E17 "
        "100.0 1080.9907552180462 1070.1850841521746 4359136.9617994055 "
        "3334088.839525756 4464532.472685248 1.6068544862341637E10 "
        "1.1728566370432955E10 1.1733314229813484E10 1.6768452787562666E10 "
        "5.830517220342475E13 4.128824258570168E13 3.8519115805773336E13 "
        "4.149420039803858E13 6.153259860972069E13 2.11108412972822656E17 "
        "1.46312985770820672E17 1.31484322773016992E17 1.31813167980595536E17 "
        "1.47560207595069728E17 2.24412785271596352E17 0.0 3840 3840 ")}
