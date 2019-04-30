import wxpymvc.model
import wxpymvc.view
import wxpymvc.controller
if __name__=="__main__":
    m=wxpymvc.model.Model()
    v=wxpymvc.view.View('z:\\Projects\\wxpymvc\\demo')
    c=wxpymvc.controller.Controller(m, v)
    c.main()
