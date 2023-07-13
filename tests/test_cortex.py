import trycortex

def test_getDocument():
    CortexAPI = trycortex.CortexAPI("sk-6834016733668d81f49444a406cf2e3c")
    print(CortexAPI.getDocument('tigers','testing.txt'))
    assert True

def test_uploadDocument():
    testing = trycortex.CreateDocument()
    testing.source_url = "https://www.test.com/"
    testing.text = "test"

    CortexAPI = trycortex.CortexAPI("sk-6834016733668d81f49444a406cf2e3c")
    print(CortexAPI.uploadDocument('tigers','newtest.txt',testing))
    assert True

def test_deleteDocument():
    CortexAPI = trycortex.CortexAPI("sk-6834016733668d81f49444a406cf2e3c")
    #print(CortexAPI.deleteDocument('tigers','newtest.txt'))
    assert True