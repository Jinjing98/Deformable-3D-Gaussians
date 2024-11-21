ModelParams = dict(
    dataset_type='endonerf',
    depth_scale=100.0,
    frame_nums=156,
    test_id=[1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97, 105, 113, 121, 129, 137, 145, 153],
    is_mask=True,
    depth_initial=True,
    accurate_mask=False,
    is_depth=True,


    # self.eval = True
    #surg-gs default update
    _white_background = True,
    #surg-gs default add
    
    #add
    # self.data_device = "cuda"
    # self.dataset_type = None
    # self.test_id = None
    # self.depth_scale = 100
    # self.is_depth = False
    # self.is_mask = False
    # self.depth_initial = False
    # self.accurate_mask = False



)
OptimizationParams = dict(
    iterations=40_000,
    densify_grad_threshold=0.0003, 
    lambda_cov=40,
    lambda_pos=0.2,

    #surg-gs default update
    lambda_smooth = 0.02,

)

# Surg-gs defulat changed bewlo:----probably need for stereomis
#  optim:
        # remove    
        # self.warm_up (= 3_000

        # update
        # self.densify_grad_threshold = 0.0002
        
        # add
        # self.lambda_smooth = 0.02
        # self.lambda_cov = 0.0
        # self.lambda_pos = 0.0
# model:
        #remove
        # self.is_blender (= False
        # self.is_6dof (= False

        #update
        # self.eval = True
        # self._white_background = True
        
        #add
        # self.data_device = "cuda"
        # self.dataset_type = None
        # self.test_id = None
        # self.depth_scale = 100
        # self.is_depth = False
        # self.is_mask = False
        # self.depth_initial = False
        # self.accurate_mask = False